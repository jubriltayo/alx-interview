#!/usr/bin/python3
""" This module contains function 'canUnlockAll' for boxes"""


def canUnlockAll(boxes):
    """
    This function determines if all boxes can be opened or not
    """
    if type(boxes) != list or len(boxes) == 0:
        return False

    box_length = len(boxes)
    free_keys = [0]
    used_keys = set()

    while free_keys:
        box_index = free_keys.pop()
        used_keys.add(box_index)
        opened_box = boxes[box_index]

        if type(opened_box) != list:
            return False

        for key in opened_box:
            if (key < box_length) and (key not in free_keys) and \
               (key not in used_keys):
                free_keys.append(key)

    return len(used_keys) == box_length
