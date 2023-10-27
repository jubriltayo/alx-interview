#!/usr/bin/python3
"""This module defines a function `validUTF8`"""


def validUTF8(data):
    """
    Checks if all elements in list is a valid UTF8 encoding

    UTF8 Format:

    1-byte sequence:   0xxxxxxx
    2-byte sequence:   110xxxxx	10xxxxxx
    3-byte sequence:   1110xxxx	10xxxxxx	10xxxxxx
    4-byte sequence:   11110xxx	10xxxxxx	10xxxxxx	10xxxxxx

    0x80 is 10000000
    0xE0 is 11100000
    OxC0 is 11000000
    0xF0 is 11110000
    0xF8 is 11111000
    """

    i = 0
    while i < len(data):
        # check if its a 1-byte data
        if data[i] & 0x80 == 0x00:
            i += 1
        # check if its a 2-byte data
        elif data[i] & 0xE0 == 0xC0:
            # check if there is a next term in the sequence and of the format
            if i + 1 >= len(data) or data[i] & 0xC0 != 0x80:
                return False
            i += 2
        # check if its a 3-byte data
        elif data[i] & 0xF0 == 0xE0:
            # check if there are 2 more terms in the sequence and of the format
            if i + 2 >= len(data) or (data[i + 1] & 0xC0 != 0x80)\
                  or (data[i + 2] & 0xC0 != 0x80):
                return False
            i + 3
        # check if its a 4-byte data
        elif data[i] & 0xF8 == 0xF0:
            # check if there are 3 more terms in the sequence and of the format
            if i + 3 >= len(data) or (data[i + 1] & 0xC0 != 0x80) or\
                  (data[i + 2] & 0xC0 != 0x80) or (data[i + 3] & 0xC0 != 0x80):
                return False
            i + 4
        else:
            return False

    return True
