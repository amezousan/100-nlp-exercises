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
    def test_write_1st_column_to_file_with_cut(self):
        nth_column    = "1"
        input_file    = filepath + filename
        output_file   = filepath + "col" + nth_column +  ".txt"
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("cut -f " + nth_column + " " + input_file, shell=True)
        expect_output = proc.decode('utf8')

        # Create colx.txt
        module.write_nth_column_to_file(nth_column, input_file)

        # Read colx.txt
        obj_output_file = open(output_file, 'r')

        # Check output file
        self.assertEqual(expect_output, obj_output_file.read())

        # Close
        obj_output_file.close()

    def test_write_2nd_column_to_file_with_cut(self):
        nth_column    = "2"
        input_file    = filepath + filename
        output_file   = filepath + "col" + nth_column +  ".txt"
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("cut -f " + nth_column + " " + input_file, shell=True)
        expect_output = proc.decode('utf8')

        # Create colx.txt
        module.write_nth_column_to_file(nth_column, input_file)

        # Read colx.txt
        obj_output_file = open(output_file, 'r')

        # Check output file
        self.assertEqual(expect_output, obj_output_file.read())

        # Close
        obj_output_file.close()

if __name__ == "__main__":
    unittest.main()