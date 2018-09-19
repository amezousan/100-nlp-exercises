#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

# Use Extended Slices: https://docs.python.org/2/whatsnew/2.3.html#extended-slices
def output(input):
    output      = ""
    output_dict = {}
    input_array = input.replace(',','')
    input_array = input_array.replace('.','')
    input_array = input_array.split(" ")

    # Convert input as dictionary
    for index, word in enumerate(input_array):
        index = str(index + 1)
        if index == "1"  or \
           index == "5"  or \
           index == "6"  or \
           index == "7"  or \
           index == "8"  or \
           index == "9"  or \
           index == "15" or \
           index == "16" or \
           index == "19":
            output_dict[index] = word[0:1]
        else:
            output_dict[index] = word[0:2]

    # Output sorted dict as string because dict cannot be sorted
    for index in range(len(output_dict)):
        index = str(index + 1)
        output = output + "%s:%s, " % (index, output_dict[index])

    # Remove the last chars
    output = output = output[:-2:]
    
    print("Input\t: " + input)
    print("Output\t: " + output)
    return output

if __name__ == "__main__":
    output(input)