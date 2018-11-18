#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

dirname          = os.path.dirname(__file__)
filepath         = os.path.join(dirname, 'resource/')
input_file       = "hightemp.txt"

# by default, tail command will return 10 lines of the top.
def tail_file(input_file, num=10):

    input_file_path  = filepath + input_file
    output           = u""

    # create obj of files
    obj_input_file = open(input_file_path, 'r')

    len_input_file = file_len(input_file_path)

    for i in range(len_input_file):
        line = obj_input_file.readline().strip()

        if (len_input_file - num) > i:
            continue

        if line:
            output += line + '\n'

    print(" - Input\t: %s"  % input_file)
    print(" - Output\t: %s" % output)

    # clear obj
    obj_input_file.close()

    return output

def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f, 1):
            pass
    return i

if __name__ == "__main__":
   tail_file(input_file)