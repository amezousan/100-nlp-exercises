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
    def test_head_default(self):
        input_file_path  = filepath + input_file

        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("head " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.head_file(input_file))

    def test_head_five_lines(self):
        input_file_path = filepath + input_file
        read_line_count = 5
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("head -n " + str(read_line_count) + " " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.head_file(input_file, read_line_count))

    def test_head_fifty_lines(self):
        input_file_path = filepath + input_file
        read_line_count = 50
        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("head -n " + str(read_line_count) + " " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.head_file(input_file, read_line_count))

    def test_head_zero_lines(self):
        input_file_path = filepath + input_file
        read_line_count = 0
        # Command below will be run on your computer with default shell
        # 
        # head -n 0 <file> returns an error
        # proc          = subprocess.check_output("head -n " + str(read_line_count) + " " + input_file_path, shell=True)
        expect_output = ""

        self.assertEqual(expect_output, module.head_file(input_file, read_line_count))

    def test_head_empty_file(self):
        empty_file      = "empty.txt"
        input_file_path = filepath + empty_file

        # Create a new empty file
        obj_input_file = open(input_file_path, 'r')
        obj_input_file.close()

        # Command below will be run on your computer with default shell
        proc          = subprocess.check_output("head " + input_file_path, shell=True)
        expect_output = proc.decode('utf8')

        self.assertEqual(expect_output, module.head_file(empty_file))

if __name__ == "__main__":
    unittest.main()