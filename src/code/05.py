#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = 'I am an NLPer'

def n_gram(str_type, ngram, input):
    # Convert a string into array, if str_type is "word", otherwise consider it as a char.
    if (str_type == "word"):
        str_array     = input.split(" ")
    else:
        str_array     = input.replace(" ", "_")

    # Common variables
    output        = ""
    str_array_len = len(str_array)

    for positon in range(str_array_len):
        # positon begins 0
        for num_of_ngram in range(ngram):
            # num_of_ngram begins 0
            if (positon + ngram) <= str_array_len:
                output = output + str_array[positon + num_of_ngram]
                # str_type "word" needs a char "-" except for the last element
                if str_type == "word" and (ngram - 1) != num_of_ngram:
                    output = output + "-"
                # If the last element, add ", "
                if (ngram - 1) == num_of_ngram:
                    output = output + ", "

    # Remove last 2 chars ", "
    output = output[:-2:]

    print("%s %s gram:" % (str_type, ngram))
    print(" - Input\t: %s" % input)
    print(" - Output\t: %s" % output)
    return output


if __name__ == "__main__":
    n_gram("word", 2, input)
    n_gram("char", 2, input)
    