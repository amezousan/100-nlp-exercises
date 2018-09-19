#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

# Use Extended Slices: https://docs.python.org/2/whatsnew/2.3.html#extended-slices
def output(input):
    output = ""
    input_array = input.replace(',','')
    input_array = input_array.replace('.','')
    input_array = input_array.split(" ")

    for char in input_array:
        output = output + str(len(char)) + " "

    # Remove the last blank
    output = output[:-1:]

    print("Input\t: " + input)
    print("Output\t: " + output)
    return output

if __name__ == "__main__":
    output(input)