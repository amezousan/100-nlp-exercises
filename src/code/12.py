#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

dirname      = os.path.dirname(__file__)
filepath     = os.path.join(dirname, 'resource/')
filename     = "hightemp.txt"

def write_nth_column_to_file(num_column, file):
    # set default column if it's empty.
    if not num_column:
        num_column = 1

    num_column      = int(num_column)
    output          = u""
    output_file     = filepath + "col" + str(num_column) + ".txt"
    obj_file        = open(file, 'r')
    obj_output_file = open(output_file, 'w')

    # https://askubuntu.com/questions/495981/access-to-column-in-python-like-awk
    for line in obj_file:
        fields = line.strip().split()
        output = output + fields[num_column - 1] + "\n"

    obj_output_file.write(output)

    print(" - Input\t: %sth column, %s"  % (num_column, file))
    print(" - Output\t: %s" % output)

    obj_file.close()
    obj_output_file.close()

    return output

if __name__ == "__main__":
   write_nth_column_to_file("1", filepath + filename)