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
    def test_setX_char_bi_gram(self):
        set_x = {'pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ad', 'di', 'is', 'se'}
        self.assertEqual(set_x, module.get_ngram_as_set("char", 2, u"paraparaparadise"))

    def test_setY_char_bi_gram(self):
        set_y = {'pa', 'ar', 'ra', 'ag', 'gr', 'ra', 'ap', 'ph'}
        self.assertEqual(set_y, module.get_ngram_as_set("char", 2, u"paragraph"))

    def test_union_from_sets(self):
        set_x  = module.get_ngram_as_set("char", 2, u"paraparaparadise")
        set_y  = module.get_ngram_as_set("char", 2, u"paragraph")
        result = {'pa', 'ar', 'ra', 'ap', 'ag', 'gr', 'ph', 'ad', 'di', 'is', 'se'}
        self.assertEqual(result, module.get_union_from_sets(set_x, set_y))

    def test_intersection_from_sets(self):
        set_x  = module.get_ngram_as_set("char", 2, u"paraparaparadise")
        set_y  = module.get_ngram_as_set("char", 2, u"paragraph")
        result = {'pa', 'ar', 'ra', 'ap'}
        self.assertEqual(result, module.get_intersection_from_sets(set_x, set_y))

    def test_set_difference_from_sets(self):
        set_x  = module.get_ngram_as_set("char", 2, u"paraparaparadise")
        set_y  = module.get_ngram_as_set("char", 2, u"paragraph")
        result = {'ad', 'di', 'is', 'se'}
        self.assertEqual(result, module.get_set_difference_from_sets(set_x, set_y))

    def test_set_difference_from_sets_reverse(self):
        set_y  = module.get_ngram_as_set("char", 2, u"paragraph")
        set_x  = module.get_ngram_as_set("char", 2, u"paraparaparadise")
        result = {'ag', 'gr', 'ph'}
        self.assertEqual(result, module.get_set_difference_from_sets(set_y, set_x))

    def test_is_included_in_set_x(self):
        set_x  = module.get_ngram_as_set("char", 2, u"paraparaparadise")
        result = True
        self.assertEqual(result, module.is_included_in_set(set_x, "se"))

    def test_is_included_in_set_y(self):
        set_y  = module.get_ngram_as_set("char", 2, u"paragraph")
        result = False
        self.assertEqual(result, module.is_included_in_set(set_y, "se"))

if __name__ == "__main__":
    unittest.main()