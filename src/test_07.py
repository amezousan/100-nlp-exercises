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
    def test_generate_sentence_with_format(self):
        input_x = 12
        input_y = u"気温"
        input_z = 22.4
        result  = u"12時の気温は22.4"
        self.assertEqual(result, module.generate_sentence_with_format(input_x, input_y, input_z))

    def test_generate_sentence_with_format_another_sentence(self):
        input_x = 14
        input_y = u"湿度"
        input_z = "80%"
        result  = u"14時の湿度は80%"
        self.assertEqual(result, module.generate_sentence_with_format(input_x, input_y, input_z))

    def test_generate_sentence_with_format_using_empty_variables(self):
        input_x = ""
        input_y = ""
        input_z = ""
        result  = u"時のは"
        self.assertEqual(result, module.generate_sentence_with_format(input_x, input_y, input_z))

if __name__ == "__main__":
    unittest.main()