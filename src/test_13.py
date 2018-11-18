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
first_file  = "col1.txt"
second_file = "col2.txt"
empty_file  = "empty.txt"

class UnitTest(unittest.TestCase):
    def setUp(self):
        print("\n# In method", self._testMethodName, ":")

    # Normal cases
    def test_merge_two_files_into_one_with_paste(self):
        first_file_path  = filepath + first_file
        second_file_path = filepath + second_file

        # Command below will be run on your computer with default shell
        output_file   = filepath + first_file + "-" + second_file + ".txt"
        proc          = subprocess.check_output("paste " + first_file_path + " " + second_file_path, shell=True)
        expect_output = proc.decode('utf8')

        # Create colx.txt
        module.merge_two_files_into_one(first_file, second_file)

        # Read colx.txt
        obj_output_file = open(output_file, 'r')

        # Check output file
        self.assertEqual(expect_output, obj_output_file.read())

        # Close
        obj_output_file.close()

    def test_in_reverse_merge_two_files_into_one_with_paste(self):
        first_file_path  = filepath + first_file
        second_file_path = filepath + second_file

        # Command below will be run on your computer with default shell
        output_file   = filepath + second_file + "-" + first_file + ".txt"
        proc          = subprocess.check_output("paste " + second_file_path + " " + first_file_path, shell=True)
        expect_output = proc.decode('utf8')

        # Create colx.txt
        module.merge_two_files_into_one(second_file, first_file)

        # Read colx.txt
        obj_output_file = open(output_file, 'r')

        # Check output file
        self.assertEqual(expect_output, obj_output_file.read())

        # Close
        obj_output_file.close()

    def test_empty_first_file_for_merge_two_files_into_one(self):
        # Set path for file
        empty_file_path  = filepath + empty_file
        second_file_path = filepath + second_file

        # New empty file
        obj_empty_file = open(empty_file_path, 'w')
        obj_empty_file.close()

        # Command below will be run on your computer with default shell
        output_file   = filepath + empty_file + "-" + second_file + ".txt"
        proc          = subprocess.check_output("paste " + empty_file_path + " " + second_file_path, shell=True)
        expect_output = proc.decode('utf8')

        # Create colx.txt
        module.merge_two_files_into_one(empty_file, second_file)

        # Read colx.txt
        obj_output_file = open(output_file, 'r')

        # Check output file
        self.assertEqual(expect_output, obj_output_file.read())

        # Close
        obj_output_file.close()

    def test_empty_second_file_for_merge_two_files_into_one(self):
        # Set path for file
        empty_file_path = filepath + empty_file
        first_file_path = filepath + first_file

        # New empty file
        obj_empty_file = open(empty_file_path, 'w')
        obj_empty_file.close()

        # Command below will be run on your computer with default shell
        output_file   = filepath + first_file + "-" + empty_file + ".txt"
        proc          = subprocess.check_output("paste " + first_file_path + " " + empty_file_path, shell=True)
        expect_output = proc.decode('utf8')

        # Create colx.txt
        module.merge_two_files_into_one(first_file, empty_file)

        # Read colx.txt
        obj_output_file = open(output_file, 'r')

        # Check output file
        self.assertEqual(expect_output, obj_output_file.read())

        # Close
        obj_output_file.close()

if __name__ == "__main__":
    unittest.main()