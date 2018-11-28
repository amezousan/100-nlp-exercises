#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

dirname          = os.path.dirname(__file__)
filepath         = os.path.join(dirname, 'resource/')
input_file       = "hightemp.txt"

# by default, split command will not split file.
def split_file(input_file_path, split_count_of_file=1):
    output           = u""

    # create obj of files
    obj_input_file = open(input_file_path, 'r')
    len_input_file = file_len(input_file_path)

    # Get split filenames
    split_filenames = determine_split_filenames(split_count_of_file)

    # If the suffix is out, then just return false.
    if split_filenames == False:
        print("error: too many files")
        obj_input_file.close()
        return False

    if len_input_file > 0:
        # Split lines into (N-1) files, after that, write out the rest into the last file.
        split_lines = int(len_input_file / split_count_of_file)
        for num_of_split_file in range(split_count_of_file - 1):
            # Initialize obj for split files
            obj_output_file = open(filepath + "split_" + split_filenames[num_of_split_file], 'w')

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
            for i in range(split_lines):
                obj_output_file.write(obj_input_file.readline())

            obj_output_file.close()

        # write out the rest into the last file
        obj_output_file = open(filepath + "split_" + split_filenames[split_count_of_file - 1], 'w')
        rest_of_lines = ('').join(obj_input_file.readlines())
        obj_output_file.write(rest_of_lines)
        obj_output_file.close()

    print(" - Input\t: %s split into %s files"  % (input_file_path, split_count_of_file))
    print(" - Output\t: %s" % split_filenames)

    # clear obj
    obj_input_file.close()

    return output

def determine_split_filenames(split_count_of_file=1):
    alphabets       = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    filenames       = []
    suffix_count    = 0
    
    # split command splits a file into "xaa", "xab"..."xba"..."xxx" according to the lines of the file.
    for i in range(split_count_of_file):
        # There are 26 chars in alphabets and i counts up from 0. If i is a multiple of 26, this means a suffix (i.e "xa") is run out, so you need to start with the next suffix (i.e. "xb").

        alphabet_count = i % 26

        if (i != 0) and (i % 26 == 0):
            suffix_count += 1

        # The suffix ends at "xzz".
        if (suffix_count > 25):
            return False

        filenames.append("x" + alphabets[suffix_count] + alphabets[alphabet_count])

    return filenames

def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f, 1):
            pass
    return i

if __name__ == "__main__":
    input_file_path  = filepath + input_file
    split_file(input_file_path, 2)