#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_first  = u'パトカー'
input_second = u'タクシー'

# Use Extended Slices: https://docs.python.org/2/whatsnew/2.3.html#extended-slices
def output(input_first, input_second):
    output = ""
    for index in range(len(input_first)):
        output = output + input_first[index:index + 1] + input_second[index:index + 1]

    print("Input\t: " + input_first, input_second)
    print("Output\t: " + output)
    return output

if __name__ == "__main__":
    output(input_first, input_second)