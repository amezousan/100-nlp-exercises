#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# title      : Set
# what to do :
#  - Create a set X and Y with "paraparaparadise" and "paragraph", using char-bi-gram.
#  - Calculate a union, intersection, and set difference between X and Y.
#  - Check if X or Y contains a bi-gram "se".
#
# terms:
#   set            : https://en.wikipedia.org/wiki/Set_(mathematics)
#   union          : https://en.wikipedia.org/wiki/Union_(set_theory)
#   intersection   : https://en.wikipedia.org/wiki/Intersection_(set_theory)
#   set difference : https://en.wikipedia.org/wiki/Complement_(set_theory)#Relative_complement
#

input_first  = 'paraparaparadise'
input_second = 'paragraph'

def get_ngram_as_set(str_type, ngram, input):
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

    # Convert an output into a set
    output = set(output.split(', '))

    print("%s %s gram:" % (str_type, ngram))
    print(" - Input\t: %s" % input)
    print(" - Output\t: %s" % output)
    return output

def get_union_from_sets(set_first, set_second):
    output = set_first.union(set_second)
    print("## Get union from sets")
    print(" - Input\t: s: %s, t: %s" % (set_first, set_second))
    print(" - Output\t: s | t: %s" % output)
    return output

def get_intersection_from_sets(set_first, set_second):
    output = set_first.intersection(set_second)
    print("## Get intersection from sets")
    print(" - Input\t: s: %s, t: %s" % (set_first, set_second))
    print(" - Output\t: s & t: %s" % output)
    return output

def get_set_difference_from_sets(set_first, set_second):
    output = set_first.difference(set_second)
    print("## Get set difference from sets")
    print(" - Input\t: s: %s, t: %s" % (set_first, set_second))
    print(" - Output\t: s - t: %s" % output)
    return output

def is_included_in_set(set, keyword):
    output = keyword in set
    print("## Is keyword included in set")
    print(" - Input\t: s: %s, keyword: %s" % (set, keyword))
    print(" - Output\t: %s" % output)
    return output

if __name__ == "__main__":
    set_x                = get_ngram_as_set("char", 2, input_first)
    set_y                = get_ngram_as_set("char", 2, input_second)
    sets_xy_union        = get_union_from_sets(set_x, set_y)
    sets_xy_intersection = get_intersection_from_sets(set_x, set_y)
    sets_xy_difference   = get_set_difference_from_sets(set_x, set_y)
    is_included_in_set_x = is_included_in_set(set_x, "se")
    is_included_in_set_y = is_included_in_set(set_y, "se")
