#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# title      : Cipher
# what to do :
#  - Implement a function "cipher" that receives characters and converts each one into another with the following specifications.
#   > Replace it as a result of "219 - the char code" if it is a lower case letter.
#   > Output other strings as they are.
#  - Encrypt and decrypt messages in English using the function "cipher".
#

input_message = u"hello2ユー!"

def cipher(message):
    # Consider a message if it's a lower case or not.
    # if it's a lower case, then ""
    output = u""
    for char in message:
        if char.islower():
            ascii_code = 219 - ord(char)
            char_code  = chr(ascii_code)
            output = output + char_code
        else:
            output = output + char

    print(" - Input\t: %s"  % message)
    print(" - Output\t: %s" % output)
    return output

if __name__ == "__main__":
    cipher(input_message)