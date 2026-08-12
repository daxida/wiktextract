# -*- fundamental -*-
#
# Tests for parsing inflection tables
#
# Copyright (c) 2021 Tatu Ylonen.  See file LICENSE and https://ylonen.org
import unittest

from wikitextprocessor import Wtp

from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.en.inflection import parse_inflection_section
from wiktextract.thesaurus import close_thesaurus_db
from wiktextract.wxr_context import WiktextractContext


class EnHyInflTests(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.wxr = WiktextractContext(Wtp(), WiktionaryConfig())
        self.wxr.wtp.start_page("testpage")
        self.wxr.wtp.start_section("English")

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()
        close_thesaurus_db(
            self.wxr.thesaurus_db_path, self.wxr.thesaurus_db_conn
        )

    def xinfl(self, word, lang, pos, section, text):
        """Runs a single inflection table parsing test, and returns ``data``."""
        self.wxr.wtp.start_page(word)
        self.wxr.wtp.start_section(lang)
        self.wxr.wtp.start_subsection(pos)
        tree = self.wxr.wtp.parse(text)
        data = {}
        parse_inflection_section(self.wxr, data, word, lang, pos, section, tree)
        return data

    def test_armenian_table_captions1(self):
        ret = self.xinfl(
            "սիրել",
            "Armenian",
            "verb",
            "Inflection",
            """<div class="inflection-table-wrapper inflection-table-red  inflection-table-collapsible inflection-table-collapsed no-vc wide" style="width: fit-content" data-toggle-category="conjugation"><templatestyles src="Template:inflection-table-top/style.css" />
{| class="inflection-table  "  
|+ class="inflection-table-title " | ''-el'' conjugation ([[w:Eastern Armenian|Eastern Armenian]])
|-

! colspan="2"  | [[անորոշ դերբայ|infinitive]]
| colspan="2" | <span class="Armn" lang="hy">սիրել</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
! colspan="2" | [[անկատար դերբայ|imperfective converb]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | [[կրավորական|passive]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրվել#Armenian|սիրվել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirvel</span><span class="mention-gloss-paren annotation-paren">)</span>
! colspan="2" | [[համակատար դերբայ|simultaneous converb]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրելիս#Armenian|սիրելիս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelis</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | [[պատճառական|causative]]
| colspan="2" | —
! colspan="2" | [[վաղակատար դերբայ|perfective converb]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | aorist stem
| colspan="2" | <span class="Armn" lang="hy">սիր-</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sir-</span><span class="mention-gloss-paren annotation-paren">)</span>
! colspan="2" | [[ապառնի դերբայ|future converb I]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | [[հարակատար դերբայ|resultative participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
! colspan="2" | [[ապառնի դերբայ|future converb II]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրելիք#Armenian|սիրելիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! colspan="2" | [[ենթակայական դերբայ|subject participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրող#Armenian|սիրող]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">siroġ</span><span class="mention-gloss-paren annotation-paren">)</span>
! colspan="2" | [[ժխտական դերբայ|connegative converb]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">siri</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
| class="separator" colspan="999" |
|-
! colspan="2" rowspan="2" | person
! colspan="3" | singular
! colspan="3" | plural

|-
! 1<sup>st</sup> person
! 2<sup>nd</sup> person
! 3<sup>rd</sup> person
! 1<sup>st</sup> person
! 2<sup>nd</sup> person
! 3<sup>rd</sup> person

|-
! rowspan="8" | [[սահմանական եղանակ|indicative]]

! colspan="1" |
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դու</span>
! <span class="Armn" lang="hy">նա</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">նրանք</span>

|-
! present
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:եմ#Armenian|եմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum em</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:ես#Armenian|ես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum es</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:է#Armenian|է]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum ē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:ենք#Armenian|ենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum enkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:եք#Armenian|եք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum ekʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:են#Armenian|են]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum en</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past imperfective
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:էի#Armenian|էի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum ēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:էիր#Armenian|էիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum ēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:էր#Armenian|էր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum ēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:էինք#Armenian|էինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum ēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:էիք#Armenian|էիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum ēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրում#Armenian|սիրում]] [[:էին#Armenian|էին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirum ēin</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! future
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:եմ#Armenian|եմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu em</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:ես#Armenian|ես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu es</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:է#Armenian|է]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu ē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:ենք#Armenian|ենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu enkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:եք#Armenian|եք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu ekʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:են#Armenian|են]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu en</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past future
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:էի#Armenian|էի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu ēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:էիր#Armenian|էիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu ēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:էր#Armenian|էր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu ēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:էինք#Armenian|էինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu ēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:էիք#Armenian|էիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu ēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]] [[:էին#Armenian|էին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu ēin</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! present perfect
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:եմ#Armenian|եմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel em</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:ես#Armenian|ես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel es</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:է#Armenian|է]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel ē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:ենք#Armenian|ենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel enkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:եք#Armenian|եք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel ekʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:են#Armenian|են]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel en</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! pluperfect
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:էի#Armenian|էի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel ēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:էիր#Armenian|էիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel ēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:էր#Armenian|էր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel ēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:էինք#Armenian|էինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel ēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:էիք#Armenian|էիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel ēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրել#Armenian|սիրել]] [[:էին#Armenian|էին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel ēin</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! aorist (past perfective)
| <span class="Armn" lang="hy">[[:սիրեցի#Armenian|սիրեցի]], [[:սիրի#Armenian|սիրի]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻi, siri&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեցիր#Armenian|սիրեցիր]], [[:սիրիր#Armenian|սիրիր]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻir, sirir&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեց#Armenian|սիրեց]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեցինք#Armenian|սիրեցինք]], [[:սիրինք#Armenian|սիրինք]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻinkʻ, sirinkʻ&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեցիք#Armenian|սիրեցիք]], [[:սիրիք#Armenian|սիրիք]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻikʻ, sirikʻ&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեցին#Armenian|սիրեցին]], [[:սիրին#Armenian|սիրին]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻin, sirin&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
|-

! rowspan="3" | [[ըղձական եղանակ|subjunctive]]
!
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դու</span>
! <span class="Armn" lang="hy">նա</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">նրանք</span>

|-
! present
| <span class="Armn" lang="hy">[[:սիրեմ#Armenian|սիրեմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirem</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրես#Armenian|սիրես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sires</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրենք#Armenian|սիրենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirenkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեք#Armenian|սիրեք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirekʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեն#Armenian|սիրեն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">siren</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! rowspan="1" | past
| <span class="Armn" lang="hy">[[:սիրեի#Armenian|սիրեի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirei</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեիր#Armenian|սիրեիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sireir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեինք#Armenian|սիրեինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sireinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեիք#Armenian|սիրեիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sireikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեին#Armenian|սիրեին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirein</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! rowspan="3" | [[պայմանական եղանակ|conditional]]
!
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դու</span>
! <span class="Armn" lang="hy">նա</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">նրանք</span>

|-
! future
| <span class="Armn" lang="hy">[[:կսիրեմ#Armenian|կսիրեմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksirem</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրես#Armenian|կսիրես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksires</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրի#Armenian|կսիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksiri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրենք#Armenian|կսիրենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksirenkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրեք#Armenian|կսիրեք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksirekʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրեն#Armenian|կսիրեն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksiren</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past
| <span class="Armn" lang="hy">[[:կսիրեի#Armenian|կսիրեի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksirei</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրեիր#Armenian|կսիրեիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksireir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրեր#Armenian|կսիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրեինք#Armenian|կսիրեինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksireinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրեիք#Armenian|կսիրեիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksireikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կսիրեին#Armenian|կսիրեին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">ksirein</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! rowspan="2" | [[հրամայական եղանակ|imperative]]
!
! —
! (<span class="Armn" lang="hy">դու</span>)
! —
! —
! (<span class="Armn" lang="hy">դուք</span>)
! —

|-
!
| —
| <span class="Armn" lang="hy">[[:սիրիր#Armenian|սիրի՛ր]], [[:սիրի#Armenian|սիրի՛]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirír, sirí&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| —
| —
| <span class="Armn" lang="hy">[[:սիրեք#Armenian|սիրե՛ք]], [[:սիրեցեք#Armenian|սիրեցե՛ք]]&#42;&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirékʻ, sirecʻékʻ&#42;&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| —
|}
<div class="inflection-table-notes">
<nowiki>*</nowiki>[[Appendix:Glossary#colloquial|colloquial]]&nbsp;&nbsp;&nbsp;**[[Appendix:Glossary#dated|dated]]<br>
</div>
</div>
<div class="inflection-table-wrapper inflection-table-red  inflection-table-collapsible inflection-table-collapsed no-vc wide" style="width: fit-content" data-toggle-category="conjugation"><templatestyles src="Template:inflection-table-top/style.css" />
{| class="inflection-table  "  
|+ class="inflection-table-title " | ''-el'' negative conjugation ([[w:Eastern Armenian|Eastern Armenian]])
|-

! colspan="2" | [[անորոշ դերբայ|infinitive]]
| colspan="2" | <span class="Armn" lang="hy">[[:չսիրել#Armenian|չսիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| colspan="4" rowspan="3" class="blank-end-row" |

|-
! colspan="2" | [[հարակատար դերբայ|resultative participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:չսիրած#Armenian|չսիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirac</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! colspan="2" | [[ենթակայական դերբայ|subject participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:չսիրող#Armenian|չսիրող]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsiroġ</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
| class="separator" colspan="999" |

|-
! colspan="2" rowspan="2" | person
! colspan="3" | singular
! colspan="3" | plural

|-
! 1<sup>st</sup> person
! 2<sup>nd</sup> person
! 3<sup>rd</sup> person
! 1<sup>st</sup> person
! 2<sup>nd</sup> person
! 3<sup>rd</sup> person

|-
! rowspan="8" | [[սահմանական եղանակ|indicative]]

! colspan="1" |
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դու</span>
! <span class="Armn" lang="hy">նա</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">նրանք</span>

|-
! present
| <span class="Armn" lang="hy">[[:չեմ#Armenian|չեմ]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻem sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չես#Armenian|չես]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻes sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չի#Armenian|չի]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻi sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չենք#Armenian|չենք]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻenkʻ sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեք#Armenian|չեք]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻekʻ sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեն#Armenian|չեն]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻen sirum</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past imperfective
| <span class="Armn" lang="hy">[[:չէի#Armenian|չէի]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēi sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիր#Armenian|չէիր]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēir sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէր#Armenian|չէր]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēr sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէինք#Armenian|չէինք]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēinkʻ sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիք#Armenian|չէիք]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēikʻ sirum</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէին#Armenian|չէին]] [[:սիրում#Armenian|սիրում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēin sirum</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! future
| <span class="Armn" lang="hy">[[:չեմ#Armenian|չեմ]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻem sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չես#Armenian|չես]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻes sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չի#Armenian|չի]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻi sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չենք#Armenian|չենք]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻenkʻ sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեք#Armenian|չեք]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻekʻ sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեն#Armenian|չեն]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻen sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past future 
| <span class="Armn" lang="hy">[[:չէի#Armenian|չէի]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēi sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիր#Armenian|չէիր]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēir sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէր#Armenian|չէր]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēr sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէինք#Armenian|չէինք]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēinkʻ sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիք#Armenian|չէիք]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēikʻ sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէին#Armenian|չէին]] [[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēin sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! present perfect
| <span class="Armn" lang="hy">[[:չեմ#Armenian|չեմ]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻem sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չես#Armenian|չես]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻes sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չի#Armenian|չի]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻi sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չենք#Armenian|չենք]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻenkʻ sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեք#Armenian|չեք]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻekʻ sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեն#Armenian|չեն]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻen sirel</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! pluperfect
| <span class="Armn" lang="hy">[[:չէի#Armenian|չէի]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēi sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիր#Armenian|չէիր]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēir sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէր#Armenian|չէր]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēr sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէինք#Armenian|չէինք]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēinkʻ sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիք#Armenian|չէիք]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēikʻ sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէին#Armenian|չէին]] [[:սիրել#Armenian|սիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēin sirel</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! aorist (past perfective)
| <span class="Armn" lang="hy">[[:չսիրեցի#Armenian|չսիրեցի]], [[:չսիրի#Armenian|չսիրի]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻi, čʻsiri&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեցիր#Armenian|չսիրեցիր]], [[:չսիրիր#Armenian|չսիրիր]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻir, čʻsirir&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեց#Armenian|չսիրեց]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեցինք#Armenian|չսիրեցինք]], [[:չսիրինք#Armenian|չսիրինք]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻinkʻ, čʻsirinkʻ&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեցիք#Armenian|չսիրեցիք]], [[:չսիրիք#Armenian|չսիրիք]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻikʻ, čʻsirikʻ&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեցին#Armenian|չսիրեցին]], [[:չսիրին#Armenian|չսիրին]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻin, čʻsirin&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
|-

! rowspan="3" | [[ըղձական եղանակ|subjunctive]]
!
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դու</span>
! <span class="Armn" lang="hy">նա</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">նրանք</span>

|-
! present
| <span class="Armn" lang="hy">[[:չսիրեմ#Armenian|չսիրեմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirem</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրես#Armenian|չսիրես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsires</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրի#Armenian|չսիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsiri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրենք#Armenian|չսիրենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirenkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեք#Armenian|չսիրեք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirekʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեն#Armenian|չսիրեն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsiren</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! rowspan="1" | past
| <span class="Armn" lang="hy">[[:չսիրեի#Armenian|չսիրեի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirei</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեիր#Armenian|չսիրեիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsireir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեր#Armenian|չսիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեինք#Armenian|չսիրեինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsireinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեիք#Armenian|չսիրեիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsireikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեին#Armenian|չսիրեին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirein</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! rowspan="3" | [[պայմանական եղանակ|conditional]]
!
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դու</span>
! <span class="Armn" lang="hy">նա</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">նրանք</span>

|-
! future
| <span class="Armn" lang="hy">[[:չեմ#Armenian|չեմ]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻem siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չես#Armenian|չես]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻes siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չի#Armenian|չի]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻi siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չենք#Armenian|չենք]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻenkʻ siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեք#Armenian|չեք]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻekʻ siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեն#Armenian|չեն]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻen siri</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past
| <span class="Armn" lang="hy">[[:չէի#Armenian|չէի]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēi siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիր#Armenian|չէիր]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēir siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէր#Armenian|չէր]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēr siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէինք#Armenian|չէինք]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēinkʻ siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիք#Armenian|չէիք]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēikʻ siri</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէին#Armenian|չէին]] [[:սիրի#Armenian|սիրի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēin siri</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! rowspan="2" | [[հրամայական եղանակ|imperative]]
!
! —
! (<span class="Armn" lang="hy">դու</span>)
! —
! —
! (<span class="Armn" lang="hy">դուք</span>)
! —

|-
!
| —
| <span class="Armn" lang="hy">[[:մի#Armenian|մի՛]] [[:սիրիր#Armenian|սիրիր]], [[:մի#Armenian|մի՛]] [[:սիրի#Armenian|սիրի]]&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">mí sirir, mí siri&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| —
| —
| <span class="Armn" lang="hy">[[:մի#Armenian|մի՛]] [[:սիրեք#Armenian|սիրեք]], [[:մի#Armenian|մի՛]] [[:սիրեցեք#Armenian|սիրեցեք]]&#42;&#42;</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">mí sirekʻ, mí sirecʻekʻ&#42;&#42;</span><span class="mention-gloss-paren annotation-paren">)</span>
| —
|}
<div class="inflection-table-notes">
<nowiki>*</nowiki>[[Appendix:Glossary#colloquial|colloquial]]&nbsp;&nbsp;&nbsp;**[[Appendix:Glossary#dated|dated]]<br>
</div>
</div>
<div class="inflection-table-wrapper inflection-table-red  inflection-table-collapsible inflection-table-collapsed no-vc " style="width: fit-content" data-toggle-category="inflection"><templatestyles src="Template:inflection-table-top/style.css" />
{| class="inflection-table  "  
|+ class="inflection-table-title " | declension of the nominalized infinitive, ''u''-type, inanimate ([[w:Eastern Armenian|Eastern Armenian]])
|-

!
! colspan=2 | singular ([[singulare tantum]])
|-
! <abbr title="includes the accusative case of traditional grammars">nominative</abbr>
| <span class="Armn" lang="hy">սիրել</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="includes the genitive case of traditional grammars">dative</abbr>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! ablative
| <span class="Armn" lang="hy">[[:սիրելուց#Armenian|սիրելուց]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelucʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! instrumental
| <span class="Armn" lang="hy">[[:սիրելով#Armenian|սիրելով]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelov</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="only used for inanimate referents">locative</abbr>
| <span class="Armn" lang="hy">[[:սիրելում#Armenian|սիրելում]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelum</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="999" class="separator" |
|-
!
! colspan="4" | definite forms
|-
! <abbr title="includes the accusative case (for inanimate referents) of traditional grammars">nominative</abbr>
| <span class="Armn" lang="hy">[[:սիրելը#Armenian|սիրելը]]&#47;[[:սիրելն#Armenian|սիրելն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelə&#47;sireln</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="includes the accusative case (for animate referents) of traditional grammars">dative</abbr>
| <span class="Armn" lang="hy">[[:սիրելուն#Armenian|սիրելուն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelun</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="999" class="separator" |
|-
!
! colspan="4" | 1<sup>st</sup> person possessive forms (my)
|-
! <abbr title="includes the accusative case of traditional grammars">nominative</abbr>
| <span class="Armn" lang="hy">[[:սիրելս#Armenian|սիրելս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirels</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="includes the genitive case of traditional grammars">dative</abbr>
| <span class="Armn" lang="hy">[[:սիրելուս#Armenian|սիրելուս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelus</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! ablative
| <span class="Armn" lang="hy">[[:սիրելուցս#Armenian|սիրելուցս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelucʻs</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! instrumental
| <span class="Armn" lang="hy">[[:սիրելովս#Armenian|սիրելովս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelovs</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="only used for inanimate referents">locative</abbr>
| <span class="Armn" lang="hy">[[:սիրելումս#Armenian|սիրելումս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelums</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="999" class="separator" |
|-
!
! colspan="4" | 2<sup>nd</sup> person possessive forms (your)
|-
! <abbr title="includes the accusative case of traditional grammars">nominative</abbr>
| <span class="Armn" lang="hy">[[:սիրելդ#Armenian|սիրելդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sireld</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="includes the genitive case of traditional grammars">dative</abbr>
| <span class="Armn" lang="hy">[[:սիրելուդ#Armenian|սիրելուդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelud</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! ablative
| <span class="Armn" lang="hy">[[:սիրելուցդ#Armenian|սիրելուցդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelucʻd</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! instrumental
| <span class="Armn" lang="hy">[[:սիրելովդ#Armenian|սիրելովդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelovd</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="only used for inanimate referents">locative</abbr>
| <span class="Armn" lang="hy">[[:սիրելումդ#Armenian|սիրելումդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelumd</span><span class="mention-gloss-paren annotation-paren">)</span>
|}

</div>
<div class="inflection-table-wrapper inflection-table-red  inflection-table-collapsible inflection-table-collapsed no-vc wide" style="width: fit-content" data-toggle-category="conjugation"><templatestyles src="Template:inflection-table-top/style.css" />
{| class="inflection-table  "  
|+ class="inflection-table-title " | plain ''-el'' conjugation ([[w:Western Armenian|Western Armenian]])
|-

! colspan="2" | [[անորոշ դերբայ|infinitive]]
| colspan="2" | <span class="Armn" lang="hy">սիրել</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
! colspan="2" | [[վաղակատար դերբայ|evidential participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | [[կրաւորական|passive]]
| colspan="2" | —
! colspan="2" | [[ապառնի դերբայ|future converb 1]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | [[պատճառական|causative]]
| colspan="2" | —
! colspan="2" | [[ապառնի դերբայ|future converb 2]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրելիք#Armenian|սիրելիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | aorist stem
| colspan="2" | <span class="Armn" lang="hy">սիր-</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sir-</span><span class="mention-gloss-paren annotation-paren">)</span>
! colspan="2" | [[ժխտական դերբայ|connegative converb (present)]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | [[յարակատար դերբայ|resultative participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
! colspan="2" | [[ժխտական դերբայ|connegative converb (past imperfect)]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="2" | [[ենթակայական դերբայ|subject participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:սիրող#Armenian|սիրող]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">siroġ</span><span class="mention-gloss-paren annotation-paren">)</span>
| class="blank-end-row" colspan="4" |
|-
| class="separator" colspan="999" |
|-
! colspan="2" rowspan="2" | person
! colspan="3" | singular
! colspan="3" | plural

|-
! 1<sup>st</sup> person
! 2<sup>nd</sup> person
! 3<sup>rd</sup> person
! 1<sup>st</sup> person
! 2<sup>nd</sup> person
! 3<sup>rd</sup> person

|-
! rowspan="10" | [[սահմանական եղանակ|indicative]]

! colspan="1" |
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դուն</span>
! <span class="Armn" lang="hy">ան</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">անոնք</span>

|-
! present
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրեմ#Armenian|սիրեմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirem</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրես#Armenian|սիրես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sires</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրէ#Armenian|սիրէ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրենք#Armenian|սիրենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirenkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրէք#Armenian|սիրէք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirēkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրեն#Armenian|սիրեն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə siren</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past imperfective
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրէի#Armenian|սիրէի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրէիր#Armenian|սիրէիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրէր#Armenian|սիրէր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրէինք#Armenian|սիրէինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրէիք#Armenian|սիրէիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:կը#Armenian|կը]] [[:սիրէին#Armenian|սիրէին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">kə sirēin</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! future
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրեմ#Armenian|սիրեմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirem</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրես#Armenian|սիրես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sires</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրէ#Armenian|սիրէ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրենք#Armenian|սիրենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirenkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրէք#Armenian|սիրէք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirēkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրեն#Armenian|սիրեն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti siren</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! past future 
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրէի#Armenian|սիրէի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրէիր#Armenian|սիրէիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրէր#Armenian|սիրէր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրէինք#Armenian|սիրէինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրէիք#Armenian|սիրէիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:սիրէին#Armenian|սիրէին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti sirēin</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! present perfect (non-evidential)
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:եմ#Armenian|եմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac em</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:ես#Armenian|ես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac es</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:է#Armenian|է]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac ē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:ենք#Armenian|ենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac enkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:էք#Armenian|էք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac ēkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:են#Armenian|են]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac en</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! pluperfect (non-evidential)
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:էի#Armenian|էի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac ēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:էիր#Armenian|էիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac ēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:էր#Armenian|էր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac ēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:էինք#Armenian|էինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac ēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:էիք#Armenian|էիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac ēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրած#Armenian|սիրած]] [[:էին#Armenian|էին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirac ēin</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! present perfect (evidential)
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:եմ#Armenian|եմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer em</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:ես#Armenian|ես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer es</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:է#Armenian|է]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer ē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:ենք#Armenian|ենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer enkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:էք#Armenian|էք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer ēkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:են#Armenian|են]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer en</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! pluperfect (evidential)
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:էի#Armenian|էի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer ēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:էիր#Armenian|էիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer ēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:էր#Armenian|էր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer ēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:էինք#Armenian|էինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer ēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:էիք#Armenian|էիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer ēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեր#Armenian|սիրեր]] [[:էին#Armenian|էին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirer ēin</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! aorist (past perfective)
| <span class="Armn" lang="hy">[[:սիրեցի#Armenian|սիրեցի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեցիր#Armenian|սիրեցիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեց#Armenian|սիրեց]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեցինք#Armenian|սիրեցինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեցիք#Armenian|սիրեցիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեցին#Armenian|սիրեցին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻin</span><span class="mention-gloss-paren annotation-paren">)</span>
|-

! rowspan="3" | [[ըղձական եղանակ|subjunctive]]
! 
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դուն</span>
! <span class="Armn" lang="hy">ան</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">անոնք</span>

|-
! present
| <span class="Armn" lang="hy">[[:սիրեմ#Armenian|սիրեմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirem</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրես#Armenian|սիրես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sires</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրէ#Armenian|սիրէ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրենք#Armenian|սիրենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirenkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրէք#Armenian|սիրէք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirēkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրեն#Armenian|սիրեն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">siren</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! rowspan="1" | past 
| <span class="Armn" lang="hy">[[:սիրէի#Armenian|սիրէի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրէիր#Armenian|սիրէիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրէր#Armenian|սիրէր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրէինք#Armenian|սիրէինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրէիք#Armenian|սիրէիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:սիրէին#Armenian|սիրէին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirēin</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! rowspan="2" | [[հրամայական եղանակ|imperative]]
! 
! —
! (<span class="Armn" lang="hy">դուն</span>)
!  —
!  —
! (<span class="Armn" lang="hy">դուք</span>)
!  —

|-
! 
| —
| <span class="Armn" lang="hy">[[:սիրէ#Armenian|սիրէ՛]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirḗ</span><span class="mention-gloss-paren annotation-paren">)</span>
| —
| —
| <span class="Armn" lang="hy">[[:սիրեցէք#Armenian|սիրեցէ՛ք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirecʻḗkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| —
|}
<div class="inflection-table-notes">
<nowiki>*</nowiki>[[Appendix:Glossary#colloquial|colloquial]]<br>
</div>
</div>
<div class="inflection-table-wrapper inflection-table-red  inflection-table-collapsible inflection-table-collapsed no-vc wide" style="width: fit-content" data-toggle-category="conjugation"><templatestyles src="Template:inflection-table-top/style.css" />
{| class="inflection-table  "  
|+ class="inflection-table-title " | plain ''-el'' negative conjugation ([[w:Western Armenian|Western Armenian]])
|-

|-
! colspan="2" | [[անորոշ դերբայ|infinitive]]
| colspan="2" | <span class="Armn" lang="hy">[[:չսիրել#Armenian|չսիրել]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirel</span><span class="mention-gloss-paren annotation-paren">)</span>
| colspan="4" rowspan="3" class="blank-end-row" |

|-
! colspan="2" | [[յարակատար դերբայ|resultative participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:չսիրած#Armenian|չսիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirac</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! colspan="2" | [[ենթակայական դերբայ|subject participle]]
| colspan="2" | <span class="Armn" lang="hy">[[:չսիրող#Armenian|չսիրող]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsiroġ</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
| class="separator" colspan="999" |
|-
! colspan="2" rowspan="2" | person
! colspan="3" | singular
! colspan="3" | plural

|-
! 1<sup>st</sup> person
! 2<sup>nd</sup> person
! 3<sup>rd</sup> person
! 1<sup>st</sup> person
! 2<sup>nd</sup> person
! 3<sup>rd</sup> person

|-
! rowspan="10" | [[սահմանական եղանակ|indicative]]

! colspan="1" |
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դուն</span>
! <span class="Armn" lang="hy">ան</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">անոնք</span>

|-
! present
| <span class="Armn" lang="hy">[[:չեմ#Armenian|չեմ]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻem sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չես#Armenian|չես]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻes sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
|  <span class="Armn" lang="hy">[[չի]] սիրեր</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻi sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չենք#Armenian|չենք]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻenkʻ sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէք#Armenian|չէք]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēkʻ sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեն#Armenian|չեն]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻen sirer</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past imperfective
| <span class="Armn" lang="hy">[[:չէի#Armenian|չէի]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēi sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիր#Armenian|չէիր]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēir sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէր#Armenian|չէր]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēr sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէինք#Armenian|չէինք]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēinkʻ sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիք#Armenian|չէիք]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēikʻ sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէին#Armenian|չէին]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēin sirer</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! future
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրեմ#Armenian|չսիրեմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirem</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրես#Armenian|չսիրես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsires</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրէ#Armenian|չսիրէ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրենք#Armenian|չսիրենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirenkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրէք#Armenian|չսիրէք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirēkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրեն#Armenian|չսիրեն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsiren</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! past future 
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրէի#Armenian|չսիրէի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրէիր#Armenian|չսիրէիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրէր#Armenian|չսիրէր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրէինք#Armenian|չսիրէինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրէիք#Armenian|չսիրէիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:պիտի#Armenian|պիտի]] [[:չսիրէին#Armenian|չսիրէին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">piti čʻsirēin</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! present perfect (non-evidential)
| <span class="Armn" lang="hy">[[:չեմ#Armenian|չեմ]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻem sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չես#Armenian|չես]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻes sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէ#Armenian|չէ]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻē sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չենք#Armenian|չենք]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻenkʻ sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէք#Armenian|չէք]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēkʻ sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեն#Armenian|չեն]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻen sirac</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! pluperfect (non-evidential)
| <span class="Armn" lang="hy">[[:չէի#Armenian|չէի]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēi sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիր#Armenian|չէիր]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēir sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէր#Armenian|չէր]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēr sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէինք#Armenian|չէինք]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēinkʻ sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիք#Armenian|չէիք]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēikʻ sirac</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէին#Armenian|չէին]] [[:սիրած#Armenian|սիրած]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēin sirac</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! present perfect (evidential)
| <span class="Armn" lang="hy">[[:չեմ#Armenian|չեմ]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻem sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չես#Armenian|չես]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻes sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէ#Armenian|չէ]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻē sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չենք#Armenian|չենք]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻenkʻ sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէք#Armenian|չէք]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēkʻ sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չեն#Armenian|չեն]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻen sirer</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! pluperfect (evidential)
| <span class="Armn" lang="hy">[[:չէի#Armenian|չէի]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēi sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիր#Armenian|չէիր]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēir sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէր#Armenian|չէր]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēr sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէինք#Armenian|չէինք]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēinkʻ sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէիք#Armenian|չէիք]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēikʻ sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չէին#Armenian|չէին]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻēin sirer</span><span class="mention-gloss-paren annotation-paren">)</span>

|-
! aorist (past perfective)
| <span class="Armn" lang="hy">[[:չսիրեցի#Armenian|չսիրեցի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեցիր#Armenian|չսիրեցիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեց#Armenian|չսիրեց]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեցինք#Armenian|չսիրեցինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեցիք#Armenian|չսիրեցիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեցին#Armenian|չսիրեցին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirecʻin</span><span class="mention-gloss-paren annotation-paren">)</span>
|-

! rowspan="3" | [[ըղձական եղանակ|subjunctive]]
! 
! <span class="Armn" lang="hy">ես</span>
! <span class="Armn" lang="hy">դուն</span>
! <span class="Armn" lang="hy">ան</span>
! <span class="Armn" lang="hy">մենք</span>
! <span class="Armn" lang="hy">դուք</span>
! <span class="Armn" lang="hy">անոնք</span>
|-
! present
| <span class="Armn" lang="hy">[[:չսիրեմ#Armenian|չսիրեմ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirem</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրես#Armenian|չսիրես]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsires</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրէ#Armenian|չսիրէ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirē</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրենք#Armenian|չսիրենք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirenkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրէք#Armenian|չսիրէք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirēkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրեն#Armenian|չսիրեն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsiren</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! rowspan="1" | past 
| <span class="Armn" lang="hy">[[:չսիրէի#Armenian|չսիրէի]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirēi</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրէիր#Armenian|չսիրէիր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirēir</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրէր#Armenian|չսիրէր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirēr</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրէինք#Armenian|չսիրէինք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirēinkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրէիք#Armenian|չսիրէիք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirēikʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| <span class="Armn" lang="hy">[[:չսիրէին#Armenian|չսիրէին]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">čʻsirēin</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! rowspan="2" | [[հրամայական եղանակ|imperative]]
! 
! —
! (<span class="Armn" lang="hy">դուն</span>)
!  —
!  —
! (<span class="Armn" lang="hy">դուք</span>)
!  —

|-
! 
| —
| <span class="Armn" lang="hy">[[:մի#Armenian|մի՛]] [[:սիրեր#Armenian|սիրեր]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">mí sirer</span><span class="mention-gloss-paren annotation-paren">)</span>
| —
| —
| <span class="Armn" lang="hy">[[:մի#Armenian|մի՛]] [[:սիրէք#Armenian|սիրէք]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">mí sirēkʻ</span><span class="mention-gloss-paren annotation-paren">)</span>
| —
|}
<div class="inflection-table-notes">
<nowiki>*</nowiki>[[Appendix:Glossary#colloquial|colloquial]]<br>
</div>
</div>
<div class="inflection-table-wrapper inflection-table-red  inflection-table-collapsible inflection-table-collapsed no-vc " style="width: fit-content" data-toggle-category="inflection"><templatestyles src="Template:inflection-table-top/style.css" />
{| class="inflection-table  "  
|+ class="inflection-table-title " | declension of the nominalized infinitive, ''u''-type, inanimate ([[w:Western Armenian|Western Armenian]])
|-

!
! colspan=2 | singular ([[singulare tantum]])
|-
! <abbr title="includes the accusative case of traditional grammars">nominative</abbr>
| <span class="Armn" lang="hy">սիրել</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirel</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="includes the genitive case of traditional grammars">dative</abbr>
| <span class="Armn" lang="hy">[[:սիրելու#Armenian|սիրելու]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelu</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! ablative
| <span class="Armn" lang="hy">[[:սիրելէ#Armenian|սիրելէ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelē</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! instrumental
| <span class="Armn" lang="hy">[[:սիրելով#Armenian|սիրելով]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelov</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="999" class="separator" |
|-
!
! colspan="4" | definite forms
|-
! <abbr title="includes the accusative case (for inanimate referents) of traditional grammars">nominative</abbr>
| <span class="Armn" lang="hy">[[:սիրելը#Armenian|սիրելը]]&#47;[[:սիրելն#Armenian|սիրելն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelə&#47;sireln</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="includes the accusative case (for animate referents) of traditional grammars">dative</abbr>
| <span class="Armn" lang="hy">[[:սիրելուն#Armenian|սիրելուն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelun</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! ablative
| <span class="Armn" lang="hy">[[:սիրելէն#Armenian|սիրելէն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelēn</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! instrumental
| <span class="Armn" lang="hy">[[:սիրելովը#Armenian|սիրելովը]]&#47;[[:սիրելովն#Armenian|սիրելովն]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelovə&#47;sirelovn</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="999" class="separator" |
|-
!
! colspan="4" | 1<sup>st</sup> person possessive forms (my)
|-
! <abbr title="includes the accusative case of traditional grammars">nominative</abbr>
| <span class="Armn" lang="hy">[[:սիրելս#Armenian|սիրելս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirels</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="includes the genitive case of traditional grammars">dative</abbr>
| <span class="Armn" lang="hy">[[:սիրելուս#Armenian|սիրելուս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelus</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! ablative
| <span class="Armn" lang="hy">[[:սիրելէս#Armenian|սիրելէս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelēs</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! instrumental
| <span class="Armn" lang="hy">[[:սիրելովս#Armenian|սիրելովս]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelovs</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! colspan="999" class="separator" |
|-
!
! colspan="4" | 2<sup>nd</sup> person possessive forms (your)
|-
! <abbr title="includes the accusative case of traditional grammars">nominative</abbr>
| <span class="Armn" lang="hy">[[:սիրելդ#Armenian|սիրելդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sireld</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! <abbr title="includes the genitive case of traditional grammars">dative</abbr>
| <span class="Armn" lang="hy">[[:սիրելուդ#Armenian|սիրելուդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelud</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! ablative
| <span class="Armn" lang="hy">[[:սիրելէդ#Armenian|սիրելէդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelēd</span><span class="mention-gloss-paren annotation-paren">)</span>
|-
! instrumental
| <span class="Armn" lang="hy">[[:սիրելովդ#Armenian|սիրելովդ]]</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="hy-Latn" class="tr Latn">sirelovd</span><span class="mention-gloss-paren annotation-paren">)</span>
|}

</div>
""",
        )
        expected = {
            "forms": [
                {
                    "form": "-el-conjugation Eastern-Armenian",
                    "source": "Inflection",
                    "tags": ["table-tags"],
                },
                {
                    "form": "սիրել",
                    "tags": ["infinitive"],
                    "source": "Inflection",
                    "roman": "sirel",
                },
                {
                    "form": "սիրում",
                    "tags": ["converb", "imperfective"],
                    "source": "Inflection",
                    "roman": "sirum",
                },
                {
                    "form": "սիրվել",
                    "tags": ["passive"],
                    "source": "Inflection",
                    "roman": "sirvel",
                },
                {
                    "form": "սիրելիս",
                    "tags": ["converb", "simultaneous"],
                    "source": "Inflection",
                    "roman": "sirelis",
                },
                {"form": "-", "tags": ["causative"], "source": "Inflection"},
                {
                    "form": "սիրել",
                    "tags": ["converb", "perfective"],
                    "source": "Inflection",
                    "roman": "sirel",
                },
                {
                    "form": "սիր-",
                    "tags": ["aorist", "stem"],
                    "source": "Inflection",
                    "roman": "sir-",
                },
                {
                    "form": "սիրելու",
                    "tags": ["converb", "converb-i", "future"],
                    "source": "Inflection",
                    "roman": "sirelu",
                },
                {
                    "form": "սիրած",
                    "tags": ["participle", "resultative"],
                    "source": "Inflection",
                    "roman": "sirac",
                },
                {
                    "form": "սիրելիք",
                    "tags": ["converb", "converb-ii", "future"],
                    "source": "Inflection",
                    "roman": "sirelikʻ",
                },
                {
                    "form": "սիրող",
                    "tags": ["participle", "subjective"],
                    "source": "Inflection",
                    "roman": "siroġ",
                },
                {
                    "form": "սիրի",
                    "tags": ["connegative", "converb"],
                    "source": "Inflection",
                    "roman": "siri",
                },
                {
                    "form": "սիրում եմ",
                    "tags": [
                        "first-person",
                        "indicative",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirum em",
                },
                {
                    "form": "սիրում ես",
                    "tags": [
                        "indicative",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirum es",
                },
                {
                    "form": "սիրում է",
                    "tags": [
                        "indicative",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirum ē",
                },
                {
                    "form": "սիրում ենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "sirum enkʻ",
                },
                {
                    "form": "սիրում եք",
                    "tags": [
                        "indicative",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirum ekʻ",
                },
                {
                    "form": "սիրում են",
                    "tags": ["indicative", "plural", "present", "third-person"],
                    "source": "Inflection",
                    "roman": "sirum en",
                },
                {
                    "form": "սիրում էի",
                    "tags": [
                        "first-person",
                        "imperfective",
                        "indicative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirum ēi",
                },
                {
                    "form": "սիրում էիր",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirum ēir",
                },
                {
                    "form": "սիրում էր",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirum ēr",
                },
                {
                    "form": "սիրում էինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "imperfective",
                        "indicative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirum ēinkʻ",
                },
                {
                    "form": "սիրում էիք",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirum ēikʻ",
                },
                {
                    "form": "սիրում էին",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirum ēin",
                },
                {
                    "form": "սիրելու եմ",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu em",
                },
                {
                    "form": "սիրելու ես",
                    "tags": [
                        "future",
                        "indicative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu es",
                },
                {
                    "form": "սիրելու է",
                    "tags": [
                        "future",
                        "indicative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu ē",
                },
                {
                    "form": "սիրելու ենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "future",
                        "indicative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu enkʻ",
                },
                {
                    "form": "սիրելու եք",
                    "tags": ["future", "indicative", "plural", "second-person"],
                    "source": "Inflection",
                    "roman": "sirelu ekʻ",
                },
                {
                    "form": "սիրելու են",
                    "tags": ["future", "indicative", "plural", "third-person"],
                    "source": "Inflection",
                    "roman": "sirelu en",
                },
                {
                    "form": "սիրելու էի",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu ēi",
                },
                {
                    "form": "սիրելու էիր",
                    "tags": [
                        "future",
                        "indicative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu ēir",
                },
                {
                    "form": "սիրելու էր",
                    "tags": [
                        "future",
                        "indicative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu ēr",
                },
                {
                    "form": "սիրելու էինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "future",
                        "indicative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu ēinkʻ",
                },
                {
                    "form": "սիրելու էիք",
                    "tags": [
                        "future",
                        "indicative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu ēikʻ",
                },
                {
                    "form": "սիրելու էին",
                    "tags": [
                        "future",
                        "indicative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirelu ēin",
                },
                {
                    "form": "սիրել եմ",
                    "tags": [
                        "first-person",
                        "indicative",
                        "perfect",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirel em",
                },
                {
                    "form": "սիրել ես",
                    "tags": [
                        "indicative",
                        "perfect",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirel es",
                },
                {
                    "form": "սիրել է",
                    "tags": [
                        "indicative",
                        "perfect",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirel ē",
                },
                {
                    "form": "սիրել ենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "sirel enkʻ",
                },
                {
                    "form": "սիրել եք",
                    "tags": [
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirel ekʻ",
                },
                {
                    "form": "սիրել են",
                    "tags": [
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirel en",
                },
                {
                    "form": "սիրել էի",
                    "tags": [
                        "first-person",
                        "indicative",
                        "pluperfect",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirel ēi",
                },
                {
                    "form": "սիրել էիր",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirel ēir",
                },
                {
                    "form": "սիրել էր",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirel ēr",
                },
                {
                    "form": "սիրել էինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "pluperfect",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirel ēinkʻ",
                },
                {
                    "form": "սիրել էիք",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirel ēikʻ",
                },
                {
                    "form": "սիրել էին",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirel ēin",
                },
                {
                    "form": "սիրեցի",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirecʻi",
                },
                {
                    "form": "սիրի",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "siri",
                },
                {
                    "form": "սիրեցիր",
                    "tags": [
                        "aorist",
                        "indicative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirecʻir",
                },
                {
                    "form": "սիրիր",
                    "tags": [
                        "aorist",
                        "indicative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirir",
                },
                {
                    "form": "սիրեց",
                    "tags": [
                        "aorist",
                        "indicative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirecʻ",
                },
                {
                    "form": "սիրեցինք",
                    "tags": [
                        "aorist",
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirecʻinkʻ",
                },
                {
                    "form": "սիրինք",
                    "tags": [
                        "aorist",
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirinkʻ",
                },
                {
                    "form": "սիրեցիք",
                    "tags": ["aorist", "indicative", "plural", "second-person"],
                    "source": "Inflection",
                    "roman": "sirecʻikʻ",
                },
                {
                    "form": "սիրիք",
                    "tags": ["aorist", "indicative", "plural", "second-person"],
                    "source": "Inflection",
                    "roman": "sirikʻ",
                },
                {
                    "form": "սիրեցին",
                    "tags": ["aorist", "indicative", "plural", "third-person"],
                    "source": "Inflection",
                    "roman": "sirecʻin",
                },
                {
                    "form": "սիրին",
                    "tags": ["aorist", "indicative", "plural", "third-person"],
                    "source": "Inflection",
                    "roman": "sirin",
                },
                {
                    "form": "սիրեմ",
                    "tags": [
                        "first-person",
                        "present",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sirem",
                },
                {
                    "form": "սիրես",
                    "tags": [
                        "present",
                        "second-person",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sires",
                },
                {
                    "form": "սիրի",
                    "tags": [
                        "present",
                        "singular",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "siri",
                },
                {
                    "form": "սիրենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "plural",
                        "present",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sirenkʻ",
                },
                {
                    "form": "սիրեք",
                    "tags": [
                        "plural",
                        "present",
                        "second-person",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sirekʻ",
                },
                {
                    "form": "սիրեն",
                    "tags": [
                        "plural",
                        "present",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "siren",
                },
                {
                    "form": "սիրեի",
                    "tags": ["first-person", "past", "singular", "subjunctive"],
                    "source": "Inflection",
                    "roman": "sirei",
                },
                {
                    "form": "սիրեիր",
                    "tags": [
                        "past",
                        "second-person",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sireir",
                },
                {
                    "form": "սիրեր",
                    "tags": ["past", "singular", "subjunctive", "third-person"],
                    "source": "Inflection",
                    "roman": "sirer",
                },
                {
                    "form": "սիրեինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "past",
                        "plural",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sireinkʻ",
                },
                {
                    "form": "սիրեիք",
                    "tags": ["past", "plural", "second-person", "subjunctive"],
                    "source": "Inflection",
                    "roman": "sireikʻ",
                },
                {
                    "form": "սիրեին",
                    "tags": ["past", "plural", "subjunctive", "third-person"],
                    "source": "Inflection",
                    "roman": "sirein",
                },
                {
                    "form": "կսիրեմ",
                    "tags": [
                        "conditional",
                        "first-person",
                        "future",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "ksirem",
                },
                {
                    "form": "կսիրես",
                    "tags": [
                        "conditional",
                        "future",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "ksires",
                },
                {
                    "form": "կսիրի",
                    "tags": [
                        "conditional",
                        "future",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "ksiri",
                },
                {
                    "form": "կսիրենք",
                    "tags": [
                        "conditional",
                        "connegative",
                        "converb",
                        "first-person",
                        "future",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "ksirenkʻ",
                },
                {
                    "form": "կսիրեք",
                    "tags": [
                        "conditional",
                        "future",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "ksirekʻ",
                },
                {
                    "form": "կսիրեն",
                    "tags": ["conditional", "future", "plural", "third-person"],
                    "source": "Inflection",
                    "roman": "ksiren",
                },
                {
                    "form": "կսիրեի",
                    "tags": ["conditional", "first-person", "past", "singular"],
                    "source": "Inflection",
                    "roman": "ksirei",
                },
                {
                    "form": "կսիրեիր",
                    "tags": [
                        "conditional",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "ksireir",
                },
                {
                    "form": "կսիրեր",
                    "tags": ["conditional", "past", "singular", "third-person"],
                    "source": "Inflection",
                    "roman": "ksirer",
                },
                {
                    "form": "կսիրեինք",
                    "tags": [
                        "conditional",
                        "connegative",
                        "converb",
                        "first-person",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "ksireinkʻ",
                },
                {
                    "form": "կսիրեիք",
                    "tags": ["conditional", "past", "plural", "second-person"],
                    "source": "Inflection",
                    "roman": "ksireikʻ",
                },
                {
                    "form": "կսիրեին",
                    "tags": ["conditional", "past", "plural", "third-person"],
                    "source": "Inflection",
                    "roman": "ksirein",
                },
                {
                    "form": "սիրի՛ր",
                    "tags": ["imperative", "rare", "singular"],
                    "source": "Inflection",
                    "roman": "sirír",
                    "links": [("սիրի՛ր", "սիրիր#Armenian")],
                },
                {
                    "form": "սիրի՛",
                    "tags": ["imperative", "rare", "singular"],
                    "source": "Inflection",
                    "roman": "sirí",
                    "links": [("սիրի՛", "սիրի#Armenian")],
                },
                {
                    "form": "սիրե՛ք",
                    "tags": ["imperative", "plural", "rare"],
                    "source": "Inflection",
                    "roman": "sirékʻ",
                    "links": [("սիրե՛ք", "սիրեք#Armenian")],
                },
                {
                    "form": "սիրեցե՛ք",
                    "tags": ["imperative", "plural", "rare"],
                    "source": "Inflection",
                    "roman": "sirecʻékʻ",
                    "links": [("սիրեցե՛ք", "սիրեցեք#Armenian")],
                },
                {
                    "form": "-el-conjugation Eastern-Armenian",
                    "source": "Inflection",
                    "tags": ["table-tags"],
                },
                {
                    "form": "չսիրել",
                    "tags": ["infinitive", "negative"],
                    "source": "Inflection",
                    "roman": "čʻsirel",
                },
                {
                    "form": "չսիրած",
                    "tags": ["negative", "participle", "resultative"],
                    "source": "Inflection",
                    "roman": "čʻsirac",
                },
                {
                    "form": "չսիրող",
                    "tags": ["negative", "participle", "subjective"],
                    "source": "Inflection",
                    "roman": "čʻsiroġ",
                },
                {
                    "form": "չեմ սիրում",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻem sirum",
                },
                {
                    "form": "չես սիրում",
                    "tags": [
                        "indicative",
                        "negative",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻes sirum",
                },
                {
                    "form": "չի սիրում",
                    "tags": [
                        "indicative",
                        "negative",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻi sirum",
                },
                {
                    "form": "չենք սիրում",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "čʻenkʻ sirum",
                },
                {
                    "form": "չեք սիրում",
                    "tags": [
                        "indicative",
                        "negative",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻekʻ sirum",
                },
                {
                    "form": "չեն սիրում",
                    "tags": [
                        "indicative",
                        "negative",
                        "plural",
                        "present",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻen sirum",
                },
                {
                    "form": "չէի սիրում",
                    "tags": [
                        "first-person",
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēi sirum",
                },
                {
                    "form": "չէիր սիրում",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēir sirum",
                },
                {
                    "form": "չէր սիրում",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēr sirum",
                },
                {
                    "form": "չէինք սիրում",
                    "tags": [
                        "first-person",
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēinkʻ sirum",
                },
                {
                    "form": "չէիք սիրում",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēikʻ sirum",
                },
                {
                    "form": "չէին սիրում",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēin sirum",
                },
                {
                    "form": "չեմ սիրելու",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "negative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻem sirelu",
                },
                {
                    "form": "չես սիրելու",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻes sirelu",
                },
                {
                    "form": "չի սիրելու",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻi sirelu",
                },
                {
                    "form": "չենք սիրելու",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "negative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻenkʻ sirelu",
                },
                {
                    "form": "չեք սիրելու",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻekʻ sirelu",
                },
                {
                    "form": "չեն սիրելու",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻen sirelu",
                },
                {
                    "form": "չէի սիրելու",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēi sirelu",
                },
                {
                    "form": "չէիր սիրելու",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēir sirelu",
                },
                {
                    "form": "չէր սիրելու",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēr sirelu",
                },
                {
                    "form": "չէինք սիրելու",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēinkʻ sirelu",
                },
                {
                    "form": "չէիք սիրելու",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēikʻ sirelu",
                },
                {
                    "form": "չէին սիրելու",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēin sirelu",
                },
                {
                    "form": "չեմ սիրել",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻem sirel",
                },
                {
                    "form": "չես սիրել",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻes sirel",
                },
                {
                    "form": "չի սիրել",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻi sirel",
                },
                {
                    "form": "չենք սիրել",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "čʻenkʻ sirel",
                },
                {
                    "form": "չեք սիրել",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻekʻ sirel",
                },
                {
                    "form": "չեն սիրել",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻen sirel",
                },
                {
                    "form": "չէի սիրել",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "pluperfect",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēi sirel",
                },
                {
                    "form": "չէիր սիրել",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēir sirel",
                },
                {
                    "form": "չէր սիրել",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēr sirel",
                },
                {
                    "form": "չէինք սիրել",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēinkʻ sirel",
                },
                {
                    "form": "չէիք սիրել",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēikʻ sirel",
                },
                {
                    "form": "չէին սիրել",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēin sirel",
                },
                {
                    "form": "չսիրեցի",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "negative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻi",
                },
                {
                    "form": "չսիրի",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "negative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsiri",
                },
                {
                    "form": "չսիրեցիր",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻir",
                },
                {
                    "form": "չսիրիր",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirir",
                },
                {
                    "form": "չսիրեց",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻ",
                },
                {
                    "form": "չսիրեցինք",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "negative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻinkʻ",
                },
                {
                    "form": "չսիրինք",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "negative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirinkʻ",
                },
                {
                    "form": "չսիրեցիք",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻikʻ",
                },
                {
                    "form": "չսիրիք",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirikʻ",
                },
                {
                    "form": "չսիրեցին",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻin",
                },
                {
                    "form": "չսիրին",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirin",
                },
                {
                    "form": "չսիրեմ",
                    "tags": [
                        "first-person",
                        "negative",
                        "present",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirem",
                },
                {
                    "form": "չսիրես",
                    "tags": [
                        "negative",
                        "present",
                        "second-person",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsires",
                },
                {
                    "form": "չսիրի",
                    "tags": [
                        "negative",
                        "present",
                        "singular",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsiri",
                },
                {
                    "form": "չսիրենք",
                    "tags": [
                        "first-person",
                        "negative",
                        "plural",
                        "present",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirenkʻ",
                },
                {
                    "form": "չսիրեք",
                    "tags": [
                        "negative",
                        "plural",
                        "present",
                        "second-person",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirekʻ",
                },
                {
                    "form": "չսիրեն",
                    "tags": [
                        "negative",
                        "plural",
                        "present",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsiren",
                },
                {
                    "form": "չսիրեի",
                    "tags": [
                        "first-person",
                        "negative",
                        "past",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirei",
                },
                {
                    "form": "չսիրեիր",
                    "tags": [
                        "negative",
                        "past",
                        "second-person",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsireir",
                },
                {
                    "form": "չսիրեր",
                    "tags": [
                        "negative",
                        "past",
                        "singular",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirer",
                },
                {
                    "form": "չսիրեինք",
                    "tags": [
                        "first-person",
                        "negative",
                        "past",
                        "plural",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsireinkʻ",
                },
                {
                    "form": "չսիրեիք",
                    "tags": [
                        "negative",
                        "past",
                        "plural",
                        "second-person",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsireikʻ",
                },
                {
                    "form": "չսիրեին",
                    "tags": [
                        "negative",
                        "past",
                        "plural",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirein",
                },
                {
                    "form": "չեմ սիրի",
                    "tags": [
                        "conditional",
                        "first-person",
                        "future",
                        "negative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻem siri",
                },
                {
                    "form": "չես սիրի",
                    "tags": [
                        "conditional",
                        "future",
                        "negative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻes siri",
                },
                {
                    "form": "չի սիրի",
                    "tags": [
                        "conditional",
                        "future",
                        "negative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻi siri",
                },
                {
                    "form": "չենք սիրի",
                    "tags": [
                        "conditional",
                        "first-person",
                        "future",
                        "negative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻenkʻ siri",
                },
                {
                    "form": "չեք սիրի",
                    "tags": [
                        "conditional",
                        "future",
                        "negative",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻekʻ siri",
                },
                {
                    "form": "չեն սիրի",
                    "tags": [
                        "conditional",
                        "future",
                        "negative",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻen siri",
                },
                {
                    "form": "չէի սիրի",
                    "tags": [
                        "conditional",
                        "first-person",
                        "negative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēi siri",
                },
                {
                    "form": "չէիր սիրի",
                    "tags": [
                        "conditional",
                        "negative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēir siri",
                },
                {
                    "form": "չէր սիրի",
                    "tags": [
                        "conditional",
                        "negative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēr siri",
                },
                {
                    "form": "չէինք սիրի",
                    "tags": [
                        "conditional",
                        "first-person",
                        "negative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēinkʻ siri",
                },
                {
                    "form": "չէիք սիրի",
                    "tags": [
                        "conditional",
                        "negative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēikʻ siri",
                },
                {
                    "form": "չէին սիրի",
                    "tags": [
                        "conditional",
                        "negative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēin siri",
                },
                {
                    "form": "մի՛ սիրիր",
                    "tags": ["imperative", "negative", "rare", "singular"],
                    "source": "Inflection",
                    "roman": "mí sirir",
                    "links": [
                        ("մի՛", "մի#Armenian"),
                        ("սիրիր", "սիրիր#Armenian"),
                    ],
                },
                {
                    "form": "մի՛ սիրի",
                    "tags": ["imperative", "negative", "rare", "singular"],
                    "source": "Inflection",
                    "roman": "mí siri",
                    "links": [
                        ("մի՛", "մի#Armenian"),
                        ("սիրի", "սիրի#Armenian"),
                    ],
                },
                {
                    "form": "մի՛ սիրեք",
                    "tags": ["imperative", "negative", "plural", "rare"],
                    "source": "Inflection",
                    "roman": "mí sirekʻ",
                    "links": [
                        ("մի՛", "մի#Armenian"),
                        ("սիրեք", "սիրեք#Armenian"),
                    ],
                },
                {
                    "form": "մի՛ սիրեցեք",
                    "tags": ["imperative", "negative", "plural", "rare"],
                    "source": "Inflection",
                    "roman": "mí sirecʻekʻ",
                    "links": [
                        ("մի՛", "մի#Armenian"),
                        ("սիրեցեք", "սիրեցեք#Armenian"),
                    ],
                },
                {
                    "form": "Eastern-Armenian inanimate infinitive noun u-type",
                    "source": "Inflection",
                    "tags": ["table-tags"],
                },
                {"form": "u-type", "source": "Inflection", "tags": ["class"]},
                {
                    "form": "սիրել",
                    "tags": ["nominative", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirel",
                },
                {
                    "form": "սիրելու",
                    "tags": ["dative", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelu",
                },
                {
                    "form": "սիրելուց",
                    "tags": ["ablative", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelucʻ",
                },
                {
                    "form": "սիրելով",
                    "tags": ["instrumental", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelov",
                },
                {
                    "form": "սիրելում",
                    "tags": ["locative", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelum",
                },
                {
                    "form": "սիրելը",
                    "tags": [
                        "definite",
                        "nominative",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                },
                {
                    "form": "սիրելն",
                    "tags": [
                        "definite",
                        "nominative",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelə/sireln",
                },
                {
                    "form": "սիրելուն",
                    "tags": ["dative", "definite", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelun",
                },
                {
                    "form": "սիրելս",
                    "tags": [
                        "first-person",
                        "nominative",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirels",
                },
                {
                    "form": "սիրելուս",
                    "tags": [
                        "dative",
                        "first-person",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelus",
                },
                {
                    "form": "սիրելուցս",
                    "tags": [
                        "ablative",
                        "first-person",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelucʻs",
                },
                {
                    "form": "սիրելովս",
                    "tags": [
                        "first-person",
                        "instrumental",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelovs",
                },
                {
                    "form": "սիրելումս",
                    "tags": [
                        "first-person",
                        "locative",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelums",
                },
                {
                    "form": "սիրելդ",
                    "tags": [
                        "nominative",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sireld",
                },
                {
                    "form": "սիրելուդ",
                    "tags": [
                        "dative",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelud",
                },
                {
                    "form": "սիրելուցդ",
                    "tags": [
                        "ablative",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelucʻd",
                },
                {
                    "form": "սիրելովդ",
                    "tags": [
                        "instrumental",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelovd",
                },
                {
                    "form": "սիրելումդ",
                    "tags": [
                        "locative",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelumd",
                },
                {
                    "form": "Western-Armenian",
                    "source": "Inflection",
                    "tags": ["table-tags"],
                },
                {
                    "form": "սիրել",
                    "tags": ["infinitive"],
                    "source": "Inflection",
                    "roman": "sirel",
                },
                {
                    "form": "սիրեր",
                    "tags": ["evidential", "participle"],
                    "source": "Inflection",
                    "roman": "sirer",
                },
                {"form": "-", "tags": ["passive"], "source": "Inflection"},
                {
                    "form": "սիրելու",
                    "tags": ["converb", "converb-i", "future"],
                    "source": "Inflection",
                    "roman": "sirelu",
                },
                {"form": "-", "tags": ["causative"], "source": "Inflection"},
                {
                    "form": "սիրելիք",
                    "tags": ["converb", "converb-ii", "future"],
                    "source": "Inflection",
                    "roman": "sirelikʻ",
                },
                {
                    "form": "սիր-",
                    "tags": ["aorist", "stem"],
                    "source": "Inflection",
                    "roman": "sir-",
                },
                {
                    "form": "սիրեր",
                    "tags": ["connegative", "converb"],
                    "source": "Inflection",
                    "roman": "sirer",
                },
                {
                    "form": "սիրած",
                    "tags": ["participle", "resultative"],
                    "source": "Inflection",
                    "roman": "sirac",
                },
                {
                    "form": "սիրող",
                    "tags": ["participle", "subjective"],
                    "source": "Inflection",
                    "roman": "siroġ",
                },
                {
                    "form": "կը սիրեմ",
                    "tags": [
                        "first-person",
                        "indicative",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirem",
                },
                {
                    "form": "կը սիրես",
                    "tags": [
                        "indicative",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "kə sires",
                },
                {
                    "form": "կը սիրէ",
                    "tags": [
                        "indicative",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirē",
                },
                {
                    "form": "կը սիրենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirenkʻ",
                },
                {
                    "form": "կը սիրէք",
                    "tags": [
                        "indicative",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirēkʻ",
                },
                {
                    "form": "կը սիրեն",
                    "tags": ["indicative", "plural", "present", "third-person"],
                    "source": "Inflection",
                    "roman": "kə siren",
                },
                {
                    "form": "կը սիրէի",
                    "tags": [
                        "first-person",
                        "imperfective",
                        "indicative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirēi",
                },
                {
                    "form": "կը սիրէիր",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirēir",
                },
                {
                    "form": "կը սիրէր",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirēr",
                },
                {
                    "form": "կը սիրէինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "imperfective",
                        "indicative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirēinkʻ",
                },
                {
                    "form": "կը սիրէիք",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirēikʻ",
                },
                {
                    "form": "կը սիրէին",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "kə sirēin",
                },
                {
                    "form": "պիտի սիրեմ",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirem",
                },
                {
                    "form": "պիտի սիրես",
                    "tags": [
                        "future",
                        "indicative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "piti sires",
                },
                {
                    "form": "պիտի սիրէ",
                    "tags": [
                        "future",
                        "indicative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirē",
                },
                {
                    "form": "պիտի սիրենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "future",
                        "indicative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirenkʻ",
                },
                {
                    "form": "պիտի սիրէք",
                    "tags": ["future", "indicative", "plural", "second-person"],
                    "source": "Inflection",
                    "roman": "piti sirēkʻ",
                },
                {
                    "form": "պիտի սիրեն",
                    "tags": ["future", "indicative", "plural", "third-person"],
                    "source": "Inflection",
                    "roman": "piti siren",
                },
                {
                    "form": "պիտի սիրէի",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirēi",
                },
                {
                    "form": "պիտի սիրէիր",
                    "tags": [
                        "future",
                        "indicative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirēir",
                },
                {
                    "form": "պիտի սիրէր",
                    "tags": [
                        "future",
                        "indicative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirēr",
                },
                {
                    "form": "պիտի սիրէինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "future",
                        "indicative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirēinkʻ",
                },
                {
                    "form": "պիտի սիրէիք",
                    "tags": [
                        "future",
                        "indicative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirēikʻ",
                },
                {
                    "form": "պիտի սիրէին",
                    "tags": [
                        "future",
                        "indicative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti sirēin",
                },
                {
                    "form": "սիրած եմ",
                    "tags": [
                        "first-person",
                        "indicative",
                        "perfect",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirac em",
                },
                {
                    "form": "սիրած ես",
                    "tags": [
                        "indicative",
                        "perfect",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirac es",
                },
                {
                    "form": "սիրած է",
                    "tags": [
                        "indicative",
                        "perfect",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirac ē",
                },
                {
                    "form": "սիրած ենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "sirac enkʻ",
                },
                {
                    "form": "սիրած էք",
                    "tags": [
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirac ēkʻ",
                },
                {
                    "form": "սիրած են",
                    "tags": [
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirac en",
                },
                {
                    "form": "սիրած էի",
                    "tags": [
                        "first-person",
                        "indicative",
                        "pluperfect",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirac ēi",
                },
                {
                    "form": "սիրած էիր",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirac ēir",
                },
                {
                    "form": "սիրած էր",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirac ēr",
                },
                {
                    "form": "սիրած էինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "pluperfect",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirac ēinkʻ",
                },
                {
                    "form": "սիրած էիք",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirac ēikʻ",
                },
                {
                    "form": "սիրած էին",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirac ēin",
                },
                {
                    "form": "սիրեր եմ",
                    "tags": [
                        "first-person",
                        "indicative",
                        "perfect",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirer em",
                },
                {
                    "form": "սիրեր ես",
                    "tags": [
                        "indicative",
                        "perfect",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirer es",
                },
                {
                    "form": "սիրեր է",
                    "tags": [
                        "indicative",
                        "perfect",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirer ē",
                },
                {
                    "form": "սիրեր ենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "sirer enkʻ",
                },
                {
                    "form": "սիրեր էք",
                    "tags": [
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirer ēkʻ",
                },
                {
                    "form": "սիրեր են",
                    "tags": [
                        "indicative",
                        "perfect",
                        "plural",
                        "present",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirer en",
                },
                {
                    "form": "սիրեր էի",
                    "tags": [
                        "first-person",
                        "indicative",
                        "pluperfect",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirer ēi",
                },
                {
                    "form": "սիրեր էիր",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirer ēir",
                },
                {
                    "form": "սիրեր էր",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirer ēr",
                },
                {
                    "form": "սիրեր էինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "pluperfect",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirer ēinkʻ",
                },
                {
                    "form": "սիրեր էիք",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirer ēikʻ",
                },
                {
                    "form": "սիրեր էին",
                    "tags": [
                        "indicative",
                        "pluperfect",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirer ēin",
                },
                {
                    "form": "սիրեցի",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirecʻi",
                },
                {
                    "form": "սիրեցիր",
                    "tags": [
                        "aorist",
                        "indicative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "sirecʻir",
                },
                {
                    "form": "սիրեց",
                    "tags": [
                        "aorist",
                        "indicative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirecʻ",
                },
                {
                    "form": "սիրեցինք",
                    "tags": [
                        "aorist",
                        "connegative",
                        "converb",
                        "first-person",
                        "indicative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "sirecʻinkʻ",
                },
                {
                    "form": "սիրեցիք",
                    "tags": ["aorist", "indicative", "plural", "second-person"],
                    "source": "Inflection",
                    "roman": "sirecʻikʻ",
                },
                {
                    "form": "սիրեցին",
                    "tags": ["aorist", "indicative", "plural", "third-person"],
                    "source": "Inflection",
                    "roman": "sirecʻin",
                },
                {
                    "form": "սիրեմ",
                    "tags": [
                        "first-person",
                        "present",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sirem",
                },
                {
                    "form": "սիրես",
                    "tags": [
                        "present",
                        "second-person",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sires",
                },
                {
                    "form": "սիրէ",
                    "tags": [
                        "present",
                        "singular",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "sirē",
                },
                {
                    "form": "սիրենք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "plural",
                        "present",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sirenkʻ",
                },
                {
                    "form": "սիրէք",
                    "tags": [
                        "plural",
                        "present",
                        "second-person",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sirēkʻ",
                },
                {
                    "form": "սիրեն",
                    "tags": [
                        "plural",
                        "present",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "siren",
                },
                {
                    "form": "սիրէի",
                    "tags": ["first-person", "past", "singular", "subjunctive"],
                    "source": "Inflection",
                    "roman": "sirēi",
                },
                {
                    "form": "սիրէիր",
                    "tags": [
                        "past",
                        "second-person",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sirēir",
                },
                {
                    "form": "սիրէր",
                    "tags": ["past", "singular", "subjunctive", "third-person"],
                    "source": "Inflection",
                    "roman": "sirēr",
                },
                {
                    "form": "սիրէինք",
                    "tags": [
                        "connegative",
                        "converb",
                        "first-person",
                        "past",
                        "plural",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "sirēinkʻ",
                },
                {
                    "form": "սիրէիք",
                    "tags": ["past", "plural", "second-person", "subjunctive"],
                    "source": "Inflection",
                    "roman": "sirēikʻ",
                },
                {
                    "form": "սիրէին",
                    "tags": ["past", "plural", "subjunctive", "third-person"],
                    "source": "Inflection",
                    "roman": "sirēin",
                },
                {
                    "form": "սիրէ՛",
                    "tags": ["imperative", "second-person", "singular"],
                    "source": "Inflection",
                    "roman": "sirḗ",
                    "links": [("սիրէ՛", "սիրէ#Armenian")],
                },
                {
                    "form": "սիրեցէ՛ք",
                    "tags": ["imperative", "plural", "rare"],
                    "source": "Inflection",
                    "roman": "sirecʻḗkʻ",
                    "links": [("սիրեցէ՛ք", "սիրեցէք#Armenian")],
                },
                {
                    "form": "Western-Armenian negative",
                    "source": "Inflection",
                    "tags": ["table-tags"],
                },
                {
                    "form": "չսիրել",
                    "tags": ["infinitive", "negative"],
                    "source": "Inflection",
                    "roman": "čʻsirel",
                },
                {
                    "form": "չսիրած",
                    "tags": ["negative", "participle", "resultative"],
                    "source": "Inflection",
                    "roman": "čʻsirac",
                },
                {
                    "form": "չսիրող",
                    "tags": ["negative", "participle", "subjective"],
                    "source": "Inflection",
                    "roman": "čʻsiroġ",
                },
                {
                    "form": "չեմ սիրեր",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻem sirer",
                },
                {
                    "form": "չես սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻes sirer",
                },
                {
                    "form": "չի սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻi sirer",
                },
                {
                    "form": "չենք սիրեր",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "čʻenkʻ sirer",
                },
                {
                    "form": "չէք սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēkʻ sirer",
                },
                {
                    "form": "չեն սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "plural",
                        "present",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻen sirer",
                },
                {
                    "form": "չէի սիրեր",
                    "tags": [
                        "first-person",
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēi sirer",
                },
                {
                    "form": "չէիր սիրեր",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēir sirer",
                },
                {
                    "form": "չէր սիրեր",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēr sirer",
                },
                {
                    "form": "չէինք սիրեր",
                    "tags": [
                        "first-person",
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēinkʻ sirer",
                },
                {
                    "form": "չէիք սիրեր",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēikʻ sirer",
                },
                {
                    "form": "չէին սիրեր",
                    "tags": [
                        "imperfective",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēin sirer",
                },
                {
                    "form": "պիտի չսիրեմ",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "negative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirem",
                },
                {
                    "form": "պիտի չսիրես",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsires",
                },
                {
                    "form": "պիտի չսիրէ",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirē",
                },
                {
                    "form": "պիտի չսիրենք",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "negative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirenkʻ",
                },
                {
                    "form": "պիտի չսիրէք",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirēkʻ",
                },
                {
                    "form": "պիտի չսիրեն",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsiren",
                },
                {
                    "form": "պիտի չսիրէի",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirēi",
                },
                {
                    "form": "պիտի չսիրէիր",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirēir",
                },
                {
                    "form": "պիտի չսիրէր",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirēr",
                },
                {
                    "form": "պիտի չսիրէինք",
                    "tags": [
                        "first-person",
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirēinkʻ",
                },
                {
                    "form": "պիտի չսիրէիք",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirēikʻ",
                },
                {
                    "form": "պիտի չսիրէին",
                    "tags": [
                        "future",
                        "indicative",
                        "negative",
                        "past",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "piti čʻsirēin",
                },
                {
                    "form": "չեմ սիրած",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻem sirac",
                },
                {
                    "form": "չես սիրած",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻes sirac",
                },
                {
                    "form": "չէ սիրած",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻē sirac",
                },
                {
                    "form": "չենք սիրած",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "čʻenkʻ sirac",
                },
                {
                    "form": "չէք սիրած",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēkʻ sirac",
                },
                {
                    "form": "չեն սիրած",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻen sirac",
                },
                {
                    "form": "չէի սիրած",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "pluperfect",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēi sirac",
                },
                {
                    "form": "չէիր սիրած",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēir sirac",
                },
                {
                    "form": "չէր սիրած",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēr sirac",
                },
                {
                    "form": "չէինք սիրած",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēinkʻ sirac",
                },
                {
                    "form": "չէիք սիրած",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēikʻ sirac",
                },
                {
                    "form": "չէին սիրած",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēin sirac",
                },
                {
                    "form": "չեմ սիրեր",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻem sirer",
                },
                {
                    "form": "չես սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻes sirer",
                },
                {
                    "form": "չէ սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "present",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻē sirer",
                },
                {
                    "form": "չենք սիրեր",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                    ],
                    "source": "Inflection",
                    "roman": "čʻenkʻ sirer",
                },
                {
                    "form": "չէք սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēkʻ sirer",
                },
                {
                    "form": "չեն սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "perfect",
                        "plural",
                        "present",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻen sirer",
                },
                {
                    "form": "չէի սիրեր",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "pluperfect",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēi sirer",
                },
                {
                    "form": "չէիր սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēir sirer",
                },
                {
                    "form": "չէր սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēr sirer",
                },
                {
                    "form": "չէինք սիրեր",
                    "tags": [
                        "first-person",
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēinkʻ sirer",
                },
                {
                    "form": "չէիք սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēikʻ sirer",
                },
                {
                    "form": "չէին սիրեր",
                    "tags": [
                        "indicative",
                        "negative",
                        "pluperfect",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻēin sirer",
                },
                {
                    "form": "չսիրեցի",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "negative",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻi",
                },
                {
                    "form": "չսիրեցիր",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻir",
                },
                {
                    "form": "չսիրեց",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "singular",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻ",
                },
                {
                    "form": "չսիրեցինք",
                    "tags": [
                        "aorist",
                        "first-person",
                        "indicative",
                        "negative",
                        "plural",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻinkʻ",
                },
                {
                    "form": "չսիրեցիք",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "plural",
                        "second-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻikʻ",
                },
                {
                    "form": "չսիրեցին",
                    "tags": [
                        "aorist",
                        "indicative",
                        "negative",
                        "plural",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirecʻin",
                },
                {
                    "form": "չսիրեմ",
                    "tags": [
                        "first-person",
                        "negative",
                        "present",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirem",
                },
                {
                    "form": "չսիրես",
                    "tags": [
                        "negative",
                        "present",
                        "second-person",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsires",
                },
                {
                    "form": "չսիրէ",
                    "tags": [
                        "negative",
                        "present",
                        "singular",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirē",
                },
                {
                    "form": "չսիրենք",
                    "tags": [
                        "first-person",
                        "negative",
                        "plural",
                        "present",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirenkʻ",
                },
                {
                    "form": "չսիրէք",
                    "tags": [
                        "negative",
                        "plural",
                        "present",
                        "second-person",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirēkʻ",
                },
                {
                    "form": "չսիրեն",
                    "tags": [
                        "negative",
                        "plural",
                        "present",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsiren",
                },
                {
                    "form": "չսիրէի",
                    "tags": [
                        "first-person",
                        "negative",
                        "past",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirēi",
                },
                {
                    "form": "չսիրէիր",
                    "tags": [
                        "negative",
                        "past",
                        "second-person",
                        "singular",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirēir",
                },
                {
                    "form": "չսիրէր",
                    "tags": [
                        "negative",
                        "past",
                        "singular",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirēr",
                },
                {
                    "form": "չսիրէինք",
                    "tags": [
                        "first-person",
                        "negative",
                        "past",
                        "plural",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirēinkʻ",
                },
                {
                    "form": "չսիրէիք",
                    "tags": [
                        "negative",
                        "past",
                        "plural",
                        "second-person",
                        "subjunctive",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirēikʻ",
                },
                {
                    "form": "չսիրէին",
                    "tags": [
                        "negative",
                        "past",
                        "plural",
                        "subjunctive",
                        "third-person",
                    ],
                    "source": "Inflection",
                    "roman": "čʻsirēin",
                },
                {
                    "form": "մի՛ սիրեր",
                    "tags": [
                        "imperative",
                        "negative",
                        "second-person",
                        "singular",
                    ],
                    "source": "Inflection",
                    "roman": "mí sirer",
                    "links": [
                        ("մի՛", "մի#Armenian"),
                        ("սիրեր", "սիրեր#Armenian"),
                    ],
                },
                {
                    "form": "մի՛ սիրէք",
                    "tags": ["imperative", "negative", "plural", "rare"],
                    "source": "Inflection",
                    "roman": "mí sirēkʻ",
                    "links": [
                        ("մի՛", "մի#Armenian"),
                        ("սիրէք", "սիրէք#Armenian"),
                    ],
                },
                {
                    "form": "Western-Armenian inanimate infinitive noun u-type",
                    "source": "Inflection",
                    "tags": ["table-tags"],
                },
                {"form": "u-type", "source": "Inflection", "tags": ["class"]},
                {
                    "form": "սիրել",
                    "tags": ["nominative", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirel",
                },
                {
                    "form": "սիրելու",
                    "tags": ["dative", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelu",
                },
                {
                    "form": "սիրելէ",
                    "tags": ["ablative", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelē",
                },
                {
                    "form": "սիրելով",
                    "tags": ["instrumental", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelov",
                },
                {
                    "form": "սիրելը",
                    "tags": [
                        "definite",
                        "nominative",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                },
                {
                    "form": "սիրելն",
                    "tags": [
                        "definite",
                        "nominative",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelə/sireln",
                },
                {
                    "form": "սիրելուն",
                    "tags": ["dative", "definite", "singular", "singular-only"],
                    "source": "Inflection",
                    "roman": "sirelun",
                },
                {
                    "form": "սիրելէն",
                    "tags": [
                        "ablative",
                        "definite",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelēn",
                },
                {
                    "form": "սիրելովը",
                    "tags": [
                        "definite",
                        "instrumental",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                },
                {
                    "form": "սիրելովն",
                    "tags": [
                        "definite",
                        "instrumental",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelovə/sirelovn",
                },
                {
                    "form": "սիրելս",
                    "tags": [
                        "first-person",
                        "nominative",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirels",
                },
                {
                    "form": "սիրելուս",
                    "tags": [
                        "dative",
                        "first-person",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelus",
                },
                {
                    "form": "սիրելէս",
                    "tags": [
                        "ablative",
                        "first-person",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelēs",
                },
                {
                    "form": "սիրելովս",
                    "tags": [
                        "first-person",
                        "instrumental",
                        "possessive",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelovs",
                },
                {
                    "form": "սիրելդ",
                    "tags": [
                        "nominative",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sireld",
                },
                {
                    "form": "սիրելուդ",
                    "tags": [
                        "dative",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelud",
                },
                {
                    "form": "սիրելէդ",
                    "tags": [
                        "ablative",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelēd",
                },
                {
                    "form": "սիրելովդ",
                    "tags": [
                        "instrumental",
                        "possessive",
                        "second-person",
                        "singular",
                        "singular-only",
                    ],
                    "source": "Inflection",
                    "roman": "sirelovd",
                },
            ]
        }

        self.assertEqual(ret, expected)
