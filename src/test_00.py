#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import importlib
import os

script_name = os.path.basename(__file__)[5:-3]
module      = importlib.import_module("code." + script_name)

class UnitTest(unittest.TestCase):
    def test_output(self):
        self.assertEqual("desserts", module.output("stressed"))

if __name__ == "__main__":
    unittest.main()