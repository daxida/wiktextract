# Tests for parse_alt_or_inflection_of()
#
# Copyright (c) 2021-2022 Tatu Ylonen.  See file LICENSE and https://ylonen.org

import unittest

from wikitextprocessor import Wtp

from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.en.form_descriptions import (
    parse_alt_or_inflection_of,
)
from wiktextract.extractor.en.page import parse_page
from wiktextract.thesaurus import close_thesaurus_db
from wiktextract.wxr_context import WiktextractContext


class FormOfTests(unittest.TestCase):
    def setUp(self):
        self.wxr = WiktextractContext(
            Wtp(lang_code="en"),
            WiktionaryConfig(
                dump_file_lang_code="en", capture_language_codes=None
            )
        )
        self.wxr.wtp.start_page("testpage")
        self.wxr.wtp.start_section("English")

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()
        close_thesaurus_db(
            self.wxr.thesaurus_db_path, self.wxr.thesaurus_db_conn
        )

    def test_non_of1(self):
        ret = parse_alt_or_inflection_of(self.wxr, "inalienable", set())
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertIs(ret, None)

    def test_non_of2(self):
        ret = parse_alt_or_inflection_of(self.wxr, "inflection of", set())
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(ret, None)

    def test_non_of3(self):
        ret = parse_alt_or_inflection_of(self.wxr, "genitive", set())
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(ret, (["genitive"], None))

    def test_simple1(self):
        ret = parse_alt_or_inflection_of(self.wxr, "abbreviation of foo", set())
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(ret, (["abbreviation", "alt-of"], [{"word": "foo"}]))

    def test_simple2(self):
        ret = parse_alt_or_inflection_of(
            self.wxr,
            "abbreviation of New York, a city in the United States",
            set(),
        )
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(
            ret,
            (
                ["abbreviation", "alt-of"],
                [{"word": "New York", "extra": "a city in the United States"}],
            ),
        )

    def test_simple3(self):
        ret = parse_alt_or_inflection_of(self.wxr, "inflection of foo", set())
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(ret, (["form-of"], [{"word": "foo"}]))

    def test_simple4(self):
        ret = parse_alt_or_inflection_of(
            self.wxr, "plural of instrumental", set()
        )
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(
            ret, (["form-of", "plural"], [{"word": "instrumental"}])
        )

    def test_simple5(self):
        ret = parse_alt_or_inflection_of(
            self.wxr, "plural of corgi or corgy", set()
        )
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(
            ret, (["form-of", "plural"], [{"word": "corgi"}, {"word": "corgy"}])
        )

    def test_simple6(self):
        ret = parse_alt_or_inflection_of(
            self.wxr, "plural of fish or chips", set()
        )
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(
            ret, (["form-of", "plural"], [{"word": "fish or chips"}])
        )

    def test_simple7(self):
        ret = parse_alt_or_inflection_of(
            self.wxr, "abbreviation of OK.", set(["OK."])
        )
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(ret, (["abbreviation", "alt-of"], [{"word": "OK."}]))

    def test_simple8(self):
        ret = parse_alt_or_inflection_of(
            self.wxr, "abbreviation of OK.", set(["OK"])
        )
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(ret, (["abbreviation", "alt-of"], [{"word": "OK"}]))

    def test_dialect1(self):
        ret = parse_alt_or_inflection_of(
            self.wxr, "Western-Armenian form of OK.", set(["OK"])
        )
        self.assertEqual(self.wxr.wtp.errors, [])
        self.assertEqual(self.wxr.wtp.warnings, [])
        self.assertEqual(self.wxr.wtp.debugs, [])
        self.assertEqual(
            ret, (["Western-Armenian", "alt-of"], [{"word": "OK"}])
        )

    def test_alt_form_section(self):
        self.wxr.wtp.add_page(
            "Template:alter",
            10,
            """<span class="Latn" lang="scn">[[zùccuru#Sicilian|zùccuru]]</span>, <span class="Latn" lang="scn">[[zùcchiru#Sicilian|zùcchiru]]</span>""",
        )
        page_data = parse_page(
            self.wxr,
            "zùccaru",
            """==Sicilian==
===Alternative forms===
* {{alter|scn|zùccuru|zùcchiru}}
===Noun===
# [[sugar]]""",
        )
        self.assertEqual(
            page_data[0]["forms"],
            [
                {"form": "zùccuru", "tags": ["alternative"]},
                {"form": "zùcchiru", "tags": ["alternative"]},
            ],
        )
