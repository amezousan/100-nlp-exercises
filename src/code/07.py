#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# title      : Generate a sentence with a format
# what to do :
#  - Implement a function to receive variables x, y, z and return a sentence "x時のyはz" filling in x, y, z with the values of the variables.
#  - Run the function with x=12, y="気温", z=22.4 and check the result.
#

input_x = 12
input_y = u"気温"
input_z = 22.4

def generate_sentence_with_format(x, y, z):
    output = u"%s時の%sは%s" % (x, y, z)
    print(" - Input\t: x - %s, y - %s, z - %s" % (x, y, z))
    print(" - Output\t: %s" % output)
    return output

if __name__ == "__main__":
    generate_sentence_with_format(input_x, input_y, input_z)