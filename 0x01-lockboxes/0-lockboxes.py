#!/usr/bin/python3
""" Module on lockboxes to determine if lockboxes can
be opened """


def canUnlockAll(boxes):
    """Function determining if all the boxes can be opened.
    Args:
        boxes (list of lists): A list rep locked boxes, where each inner list
                               contains keys to other boxes.
    Returns:
        bool: True if all boxes can be opened, False otherwise
    """

    keys = [0]
    """ list keys initialized with the first box (box 0) as unlocked.
    Keys stores indices of unlocked and accessible boxes """
    for key in keys:
        """ For each key, it accesses the corresponding box in boxes """
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        """checking is numbe of keys equals number of boxes """
        return True
    return False
