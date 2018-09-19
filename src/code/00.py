#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = "stressed"

# Use Extended Slices: https://docs.python.org/2/whatsnew/2.3.html#extended-slices
def output(input):
    output = input[::-1]
    print("Input\t: " + input)
    print("Output\t: " + output)
    return output

if __name__ == "__main__":
    output(input)