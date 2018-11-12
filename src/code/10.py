#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# title      : count lines of file
# what to do :
#  - You need to replace tabs in the file "hightemp.txt", which includes "prefectures" "area" "temperature" "day" of Japan.
#  - You need to verify the result with linux command sed, tr or expand.
#
import os

dirname  = os.path.dirname(__file__)
filepath = os.path.join(dirname, 'resource/')
filename = "hightemp.txt"

def count_up_line_of_file(file):
    output   = 0
    obj_file = open(file, 'r')
    
    for line in obj_file:
        output = output + 1

    print(" - Input\t: %s"  % file)
    print(" - Output\t: %s" % output)

    obj_file.close()

    return output

if __name__ == "__main__":
   count_up_line_of_file(filepath + filename)