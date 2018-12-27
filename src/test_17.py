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

    # 1   2   3   4
    # -------------
    # 1a
    # 1b
    # 1c
    # .
    # .
    # .
    # 1n
    #
    # 1. List all the items (1a...1n)
    # 2. Sort the List
    # 3. Uniq the list

    def test_uniq_1st_row(self):
        input_file_path = filepath + input_file
        proc            = subprocess.check_output("awk '{print $1}' " + input_file_path + " | sort | uniq", shell=True)
        expect_output   = set(proc.decode().strip().split("\n"))

        self.assertEqual(expect_output, module.uniq_nth_row(1, input_file_path))

    def test_uniq_2nd_row(self):
        input_file_path = filepath + input_file
        proc            = subprocess.check_output("awk '{print $2}' " + input_file_path + " | sort | uniq", shell=True)
        expect_output   = set(proc.decode().strip().split("\n"))

        self.assertEqual(expect_output, module.uniq_nth_row(2, input_file_path))

    def test_uniq_3rd_row(self):
        input_file_path = filepath + input_file
        proc            = subprocess.check_output("awk '{print $3}' " + input_file_path + " | sort | uniq", shell=True)
        expect_output   = set(proc.decode().strip().split("\n"))

        self.assertEqual(expect_output, module.uniq_nth_row(3, input_file_path))

if __name__ == "__main__":
    unittest.main()