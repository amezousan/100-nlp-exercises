#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

dirname          = os.path.dirname(__file__)
filepath         = os.path.join(dirname, 'resource/')
first_file       = "col1.txt"
second_file      = "col2.txt"

def merge_two_files_into_one(first_file, second_file):
    # set default args if it's empty.
    # ToDo
    first_file_path  = filepath + first_file
    second_file_path = filepath + second_file
    output           = u""
    output_file      = filepath + first_file + "-" + second_file + ".txt"

    # create obj of files
    obj_first_file   = open(first_file_path, 'r')
    obj_second_file  = open(second_file_path, 'r')
    obj_output_file  = open(output_file, 'w')

    # Get max line of file
    first_file_lines  = file_len(first_file_path)
    second_file_lines = file_len(second_file_path)
    max_line_of_file  = first_file_lines if first_file_lines >= second_file_lines else second_file_lines

    for i in range(max_line_of_file):
        output += obj_first_file.readline().strip() + '\t' + obj_second_file.readline().strip() + '\n'

    # Create the output file
    obj_output_file.write(output)

    print(" - Input\t: merge %s and %s into %s"  % (first_file, second_file, output_file))
    print(" - Output\t: %s" % output)

    # clear obj
    obj_first_file.close()
    obj_second_file.close()
    obj_output_file.close()

    return output

# https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f, 1):
            pass
    return i

if __name__ == "__main__":
   merge_two_files_into_one(first_file, second_file)