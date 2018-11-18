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
input_file  = "hightemp.txt"

class UnitTest(unittest.TestCase):
    def setUp(self):
        print("\n# In method", self._testMethodName, ":")

    # Normal cases
    def test_tail_default(self):
        input_file_path  = filepath + input_file

        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("tail " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.tail_file(input_file))

    def test_tail_five_lines(self):
        input_file_path = filepath + input_file
        read_line_count = 5
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("tail -n " + str(read_line_count) + " " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.tail_file(input_file, read_line_count))

    def test_tail_fifty_lines(self):
        input_file_path = filepath + input_file
        read_line_count = 50
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("tail -n " + str(read_line_count) + " " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.tail_file(input_file, read_line_count))

    def test_tail_zero_lines(self):
        input_file_path = filepath + input_file
        read_line_count = 0
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("tail -n " + str(read_line_count) + " " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.tail_file(input_file, read_line_count))

    def test_tail_empty_file(self):
        empty_file      = "empty.txt"
        input_file_path = filepath + empty_file

        # Create a new empty file
        obj_input_file = open(input_file_path, 'r')
        obj_input_file.close()

        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("tail " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.tail_file(empty_file))

if __name__ == "__main__":
    unittest.main()