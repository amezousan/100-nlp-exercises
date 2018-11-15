#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

dirname  = os.path.dirname(__file__)
filepath = os.path.join(dirname, 'resource/')
filename = "hightemp.txt"

def replace_tab_by_space(file):
    output   = u""
    obj_file = open(file, 'r')
    
    for line in obj_file:
        output = output + re.sub('\t', ' ', line)

    print(" - Input\t: %s"  % file)
    print(" - Output\t: %s" % output)

    obj_file.close()

    return output

if __name__ == "__main__":
   replace_tab_by_space(filepath + filename)