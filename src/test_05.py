#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import importlib
import os

script_name = os.path.basename(__file__)[5:-3]
module      = importlib.import_module("code." + script_name)

class UnitTest(unittest.TestCase):
    def setUp(self):
        print("\n# In method", self._testMethodName, ":")

    # Normal cases
    def test_word_bi_gram(self):
        self.assertEqual(u"I-am, am-an, an-NLPer", module.n_gram("word", 2, u"I am an NLPer"))

    def test_char_bi_gram(self):
        self.assertEqual(u"I_, _a, am, m_, _a, an, n_, _N, NL, LP, Pe, er", module.n_gram("char", 2, u"I am an NLPer"))

    def test_word_bi_gram_another_sentence(self):
        self.assertEqual(u"Hi-nice, nice-to, to-meet, meet-you", module.n_gram("word", 2, u"Hi nice to meet you"))

    def test_char_bi_gram_another_sentence(self):
        self.assertEqual(u"Hi, i_, _n, ni, ic, ce, e_, _t, to, o_, _m, me, ee, et, t_, _y, yo, ou", module.n_gram("char", 2, u"Hi nice to meet you"))

    def test_word_tri_gram(self):
        self.assertEqual(u"I-am-an, am-an-NLPer", module.n_gram("word", 3, u"I am an NLPer"))

    def test_char_tri_gram(self):
        self.assertEqual(u"I_a, _am, am_, m_a, _an, an_, n_N, _NL, NLP, LPe, Per", module.n_gram("char", 3, u"I am an NLPer"))

    # Anormaly cases
    def test_word_bi_gram_with_specialchars(self):
        self.assertEqual(u"Hi,-nice, nice-to, to-meet, meet-you!", module.n_gram("word", 2, u"Hi, nice to meet you!"))

    def test_char_bi_gram_with_specialchars(self):
        self.assertEqual(u"Hi, i,, ,_, _n, ni, ic, ce, e_, _t, to, o_, _m, me, ee, et, t_, _y, yo, ou, u!", module.n_gram("char", 2, u"Hi, nice to meet you!"))


if __name__ == "__main__":
    unittest.main()