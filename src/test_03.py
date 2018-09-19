#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import importlib
import os

script_name = os.path.basename(__file__)[5:-3]
module      = importlib.import_module("code." + script_name)

class UnitTest(unittest.TestCase):
    def test_output(self):
        self.assertEqual(u"3 1 4 1 5 9 2 6 5 3 5 8 9 7 9", module.output(u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))

if __name__ == "__main__":
    unittest.main()