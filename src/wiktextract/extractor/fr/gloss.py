from collections import defaultdict
from typing import Dict, List

from wikitextprocessor import NodeKind, WikiNode
from wikitextprocessor.parser import TemplateNode
from wiktextract.page import clean_node
from wiktextract.wxr_context import WiktextractContext


def extract_gloss(
    wxr: WiktextractContext,
    page_data: List[Dict],
    list_node: WikiNode,
) -> None:
    for list_item_node in list_node.find_child(NodeKind.LIST_ITEM):
        gloss_nodes = list(
            list_item_node.invert_find_child(
                NodeKind.LIST, include_empty_str=True
            )
        )
        gloss_data = defaultdict(list)
        gloss_start = 0
        # process modifier, theme tempaltes before gloss text
        # https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_tous_les_modèles/Précisions_de_sens
        for index, gloss_node in enumerate(gloss_nodes):
            if isinstance(gloss_node, TemplateNode):
                categories_data = defaultdict(list)
                expanded_text = clean_node(wxr, categories_data, gloss_node)
                if expanded_text.startswith("(") and expanded_text.endswith(
                    ")"
                ):
                    gloss_start = index + 1
                    tag = expanded_text.strip("() \n")
                    if len(tag) > 0:
                        gloss_data["tags"].append(tag)
                    if "categories" in categories_data:
                        gloss_data["categories"].extend(
                            categories_data["categories"]
                        )

        gloss_only_nodes = []
        tag_indexes = set()
        for index, node in enumerate(gloss_nodes[gloss_start:], gloss_start):
            # if an italic node is between parentheses then it's a tag, also
            # don't add the parenthese strings to `gloss_only_nodes`
            if (
                isinstance(node, WikiNode)
                and node.kind == NodeKind.ITALIC
                and index > gloss_start
                and isinstance(gloss_nodes[index - 1], str)
                and gloss_nodes[index - 1].strip() == "("
                and index + 1 < len(gloss_nodes)
                and isinstance(gloss_nodes[index + 1], str)
                and gloss_nodes[index + 1].strip() == ")"
            ):
                gloss_data["tags"].append(clean_node(wxr, None, node))
                tag_indexes |= {index - 1, index, index + 1}
                continue

        gloss_only_nodes = [
            node
            for index, node in enumerate(gloss_nodes[gloss_start:], gloss_start)
            if index not in tag_indexes
        ]
        gloss_text = clean_node(wxr, gloss_data, gloss_only_nodes)
        gloss_data["glosses"] = [gloss_text]
        extract_examples(wxr, gloss_data, list_item_node)
        page_data[-1]["senses"].append(gloss_data)


def extract_examples(
    wxr: WiktextractContext,
    gloss_data: Dict,
    gloss_list_node: WikiNode,
) -> None:
    for example_node in gloss_list_node.find_child_recursively(
        NodeKind.LIST_ITEM
    ):
        example_node_children = list(example_node.filter_empty_str_child())
        if len(example_node_children) == 0:
            continue
        first_child = example_node_children[0]
        if (
            isinstance(first_child, WikiNode)
            and first_child.kind == NodeKind.TEMPLATE
            and first_child.template_name == "exemple"
        ):
            process_exemple_template(wxr, first_child, gloss_data)
        else:
            example_nodes = []
            source_template = None
            for example_template in example_node.find_child(NodeKind.TEMPLATE):
                if example_template.template_name == "source":
                    source_template = example_template
            example_nodes = [
                node
                for node in example_node_children
                if node != source_template
            ]
            example_data = {"type": "example"}
            example_data["text"] = clean_node(wxr, None, example_nodes)
            if source_template is not None:
                example_data["ref"] = clean_node(
                    wxr, None, source_template
                ).strip("— ()")
                example_data["type"] = "quotation"
            gloss_data["examples"].append(example_data)


def process_exemple_template(
    wxr: WiktextractContext, node: TemplateNode, gloss_data: Dict
) -> None:
    # https://fr.wiktionary.org/wiki/Modèle:exemple
    # https://fr.wiktionary.org/wiki/Modèle:ja-exemple
    # https://fr.wiktionary.org/wiki/Modèle:zh-exemple
    text = clean_node(wxr, None, node.template_parameters.get(1, ""))
    translation = clean_node(
        wxr,
        None,
        node.template_parameters.get(
            2, node.template_parameters.get("sens", "")
        ),
    )
    transcription = clean_node(
        wxr,
        None,
        node.template_parameters.get(3, node.template_parameters.get("tr", "")),
    )
    source = clean_node(wxr, None, node.template_parameters.get("source", ""))
    example_data = {"type": "example"}
    if len(text) > 0:
        example_data["text"] = clean_node(wxr, None, text)
    if len(translation) > 0:
        example_data["translation"] = clean_node(wxr, None, translation)
    if len(transcription) > 0:
        example_data["roman"] = clean_node(wxr, None, transcription)
    if len(source) > 0:
        example_data["ref"] = clean_node(wxr, None, source)
        example_data["type"] = "quotation"
    if "text" in example_data:
        gloss_data["examples"].append(example_data)