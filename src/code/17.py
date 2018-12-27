#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

dirname          = os.path.dirname(__file__)
filepath         = os.path.join(dirname, 'resource/')
input_file       = "hightemp.txt"

# by default, split command will not split file.
def uniq_nth_row(num_column, input_file_path):
    output = ""

    # create obj of files
    obj_input_file = open(input_file_path, 'r')
    num_column     = int(num_column)

    output = set(output)

    for line in obj_input_file:
        fields = line.strip().split()
        output.add(fields[num_column - 1])

    print(" - Input\t: %s"  % input_file_path)
    print(" - Output\t: %s" % output)

    # clear obj
    obj_input_file.close()

    return output

if __name__ == "__main__":
    input_file_path  = filepath + input_file
    uniq_nth_row(1, input_file_path)