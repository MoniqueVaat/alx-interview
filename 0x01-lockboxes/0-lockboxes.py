#!/usr/bin/python3
"""Method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened.
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, else return False
    """
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
