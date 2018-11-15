#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import importlib
import os
import subprocess
import sys

script_name = os.path.basename(__file__)[5:-3]
module      = importlib.import_module("code." + script_name)
dirname     = os.path.dirname(__file__)
filepath    = os.path.join(dirname, 'code/resource/')
filename    = "hightemp.txt"

class UnitTest(unittest.TestCase):
    def setUp(self):
        print("\n# In method", self._testMethodName, ":")

    # Normal cases
    def test_replace_tab_by_space_with_expand(self):
        input_file    = filepath + filename
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("expand -t 1 " + input_file, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.replace_tab_by_space(input_file))

    def test_replace_tab_by_space_with_tr(self):
        input_file    = filepath + filename
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("tr '\t' ' ' < " + input_file, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.replace_tab_by_space(input_file))

    def test_replace_tab_by_space_with_sed(self):
        input_file    = filepath + filename
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("sed -e s/\t/ /g " + input_file, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.replace_tab_by_space(input_file))

if __name__ == "__main__":
    unittest.main()