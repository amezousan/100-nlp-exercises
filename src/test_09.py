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
    def test_total_length(self):
        input_message  = "Hello my name is John."
        expect_length  = len(input_message)
        self.assertEqual(expect_length, len(module.rearrange_chars(input_message)))

if __name__ == "__main__":
    unittest.main()