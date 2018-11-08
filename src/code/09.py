#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# title      : Typoglycemia
# what to do :
#  - For word strings separated by spaces, create a program that randomly rearranges the order of other characters, leaving the beginning and end letters of each word. But a word whose length is 4 or less is not re-arranged
#  - Give an appropriate English sentence (e.g. "I could not believe that I think actually understand what I was reading: the phenomenal power of the human mind.") and confirm the execution result.
#
import random

input_message = u"I could not believe that I think actually understand what I was reading: the phenomenal power of the human mind."

def rearrange_chars(chars):
    # Convert input(str) into array
    input_array = chars.split(" ")
    output      = u""

    for char in input_array:
        len_char = len(char)
        # If a word whose length is 5 or more, rearrange it.
        if len_char > 4:
            char_first = char[0]
            char_last  = char[-1]
            char_rest  = char[1:-1]
            # print("First: %s, Last: %s, Rest: %s" % (char_first, char_last, char_rest))
            char_rest = random.sample(char_rest, len_char - 2)
            output = output + char_first + ('').join(char_rest) + char_last
        else:
            output = output + char

        # Add spaces between words
        output = output + ' '

    # Remove the space of the last word
    output = output[:-1:]

    print(" - Input\t: %s"  % chars)
    print(" - Output\t: %s" % output)
    return output

if __name__ == "__main__":
    rearrange_chars(input_message)