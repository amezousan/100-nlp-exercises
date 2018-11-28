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
testcode_path = os.path.join(dirname, '')

class UnitTest(unittest.TestCase):
    def setUp(self):
        print("\n# In method", self._testMethodName, ":")

    # Normal cases
    def test_split_filenames_three(self):
        split_count_of_file = 3
        expect_output       = ['xaa', 'xab', 'xac']

        print(expect_output)

        self.assertEqual(expect_output, module.determine_split_filenames(split_count_of_file))

    def test_split_filenames_thirty(self):
        split_count_of_file = 30
        expect_output       = ['xaa', 'xab', 'xac', 'xad', 'xae', 'xaf', 'xag', 'xah', 'xai', 'xaj', 'xak', 'xal', 'xam', 'xan', 'xao', 'xap', 'xaq', 'xar', 'xas', 'xat', 'xau', 'xav', 'xaw', 'xax', 'xay', 'xaz', 'xba', 'xbb', 'xbc', 'xbd']

        print(expect_output)

        self.assertEqual(expect_output, module.determine_split_filenames(split_count_of_file))

    def test_split_filenames_thousand(self):
        # split command will return an error "split: too many files", if it cannot split a file over the limitation of the suffix.
        split_count_of_file = 1000

        self.assertFalse(module.determine_split_filenames(split_count_of_file))

    def test_split_empty_file(self):
        # Initialize empty file
        input_file_path = filepath + "empty.txt"
        obj_input_file  = open(input_file_path, 'w')
        obj_input_file.close()

        # if it's empty, split command will not do anything.
        prefix_split_file = filepath + "split_test_empty_x"
        proc              = subprocess.check_output("split " + input_file_path + " " + prefix_split_file, shell=True)
        expect_output     = ""

        self.assertEqual(expect_output, module.split_file(input_file_path))

    def test_split_file_without_options(self):
        prefix_split_file = filepath + "split_test_x"
        input_file_path   = filepath + input_file
        # proc              = subprocess.check_output("split " + input_file_path + " " + prefix_split_file, shell=True)
        ###
        # Let's imagine what the file should be split.
        #
        # i.e.) Num of files(N) = 1, Lines(L) = 10, File's lines(F) = {10}
        # N = 2, L = 10, F = {5,5}
        # N = 3, L = 10, F = {3,3,4}
        # N = 4, L = 10, F = {2,2,2,4}
        # N = 5, L = 10, F = {2,2,2,2,2}
        #
        # In this case, (N-1) files have (L/N) lines and N file has the rest of the file.
        ###
        # i.e. ['xaa', 'xab' ...]
        split_count_of_file = 1
        split_filenames     = module.determine_split_filenames(split_count_of_file)
        len_input_file      = module.file_len(input_file_path)
        split_lines         = int(len_input_file / split_count_of_file)

        module.split_file(input_file_path)
        proc = subprocess.check_output("split -l " + str(split_lines) + " " + input_file_path + " " + prefix_split_file, shell=True)

        obj_input_file = open(filepath + 'split_xaa')
        expect_output  = obj_input_file.read()
        obj_input_file.close()

        obj_output_file = open(filepath + 'split_test_xaa')
        expect_proc     = obj_output_file.read()
        obj_output_file.close()

        self.assertEqual(expect_output, expect_proc)

    def test_split_file_into_ten(self):
        prefix_split_file = filepath + "split_test_x"
        input_file_path   = filepath + input_file
        # proc              = subprocess.check_output("split " + input_file_path + " " + prefix_split_file, shell=True)
        ###
        # Let's imagine what the file should be split.
        #
        # i.e.) Num of files(N) = 1, Lines(L) = 10, File's lines(F) = {10}
        # N = 2, L = 10, F = {5,5}
        # N = 3, L = 10, F = {3,3,4}
        # N = 4, L = 10, F = {2,2,2,4}
        # N = 5, L = 10, F = {2,2,2,2,2}
        #
        # In this case, (N-1) files have (L/N) lines and N file has the rest of the file.
        ###
        # i.e. ['xaa', 'xab' ...]
        split_count_of_file = 10
        split_filenames     = module.determine_split_filenames(split_count_of_file)
        len_input_file      = module.file_len(input_file_path)
        split_lines         = int(len_input_file / split_count_of_file)

        module.split_file(input_file_path, split_count_of_file)
        proc = subprocess.check_output("split -l " + str(split_lines) + " " + input_file_path + " " + prefix_split_file, shell=True)

        # It's enought to check the N-1 files.
        for num_of_split_file in range(split_count_of_file - 1):
            obj_input_file = open(filepath + 'split_' + split_filenames[num_of_split_file])
            expect_output  = obj_input_file.read()
            obj_input_file.close()

            obj_output_file = open(filepath + 'split_test_' + split_filenames[num_of_split_file])
            expect_proc     = obj_output_file.read()
            obj_output_file.close()

            self.assertEqual(expect_output, expect_proc)

    def test_split_file_into_twenty(self):
        prefix_split_file = filepath + "split_test_x"
        input_file_path   = filepath + input_file
        # proc              = subprocess.check_output("split " + input_file_path + " " + prefix_split_file, shell=True)
        ###
        # Let's imagine what the file should be split.
        #
        # i.e.) Num of files(N) = 1, Lines(L) = 10, File's lines(F) = {10}
        # N = 2, L = 10, F = {5,5}
        # N = 3, L = 10, F = {3,3,4}
        # N = 4, L = 10, F = {2,2,2,4}
        # N = 5, L = 10, F = {2,2,2,2,2}
        #
        # In this case, (N-1) files have (L/N) lines and N file has the rest of the file.
        ###
        # i.e. ['xaa', 'xab' ...]
        split_count_of_file = 20
        split_filenames     = module.determine_split_filenames(split_count_of_file)
        len_input_file      = module.file_len(input_file_path)
        split_lines         = int(len_input_file / split_count_of_file)

        module.split_file(input_file_path, split_count_of_file)
        proc = subprocess.check_output("split -l " + str(split_lines) + " " + input_file_path + " " + prefix_split_file, shell=True)

        # It's enought to check the N-1 files.
        for num_of_split_file in range(split_count_of_file - 1):
            obj_input_file = open(filepath + 'split_' + split_filenames[num_of_split_file])
            expect_output  = obj_input_file.read()
            obj_input_file.close()

            obj_output_file = open(filepath + 'split_test_' + split_filenames[num_of_split_file])
            expect_proc     = obj_output_file.read()
            obj_output_file.close()

            self.assertEqual(expect_output, expect_proc)

    def test_split_file_into_thousand(self):
        input_file_path   = filepath + input_file
        split_count_of_file = 1000
        self.assertFalse(module.split_file(input_file_path, split_count_of_file))

if __name__ == "__main__":
    unittest.main()