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
    def test_count_up_lines_with_wc(self):
        input_file    = filepath + filename
        # The commands will be run on your computer with default shell, so you may need to install wc and awk command.
        proc          = subprocess.check_output("wc -l < " + input_file + " | awk '{print $1}'", shell=True)
        expect_output = int(proc.decode('utf8').rstrip())

        self.assertEqual(expect_output, module.count_up_line_of_file(input_file))

if __name__ == "__main__":
    unittest.main()