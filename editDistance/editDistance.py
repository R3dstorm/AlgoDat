#!/usr/bin/python3

import sys


def compute_ed_recursively(x, y):
    """ Compute edit distance from x to y recursively.

    >>> compute_ed_recursively("", "")
    0
    >>> compute_ed_recursively("donald", "ronaldo")
    2
    """
    n = len(x)
    m = len(y)
    if n == 0:
        return m
    if m == 0:
        return n
    # Insert case.
    ed1 = compute_ed_recursively(x, y[0:-1]) + 1
    # Delete case.
    ed2 = compute_ed_recursively(x[0:-1], y) + 1
    # Replace case.
    ed3 = compute_ed_recursively(x[0:-1], y[0:-1])
    # If last characters do not match, add replace costs.
    if x[-1] != y[-1]:
        ed3 += 1
    return min(ed1, ed2, ed3)


def compute_ed_via_table(x, y):
    """ Compute edit distance via dynamic programming table.

    >>> compute_ed_via_table("", "")
    0
    >>> compute_ed_via_table("RAUM", "GRAU")
    2
    >>> compute_ed_via_table("ABCDEFGHIJKLMNOPQRSTUV", "ABCDEFGHIJKLMNOPQRSTUVK")
    0
    """
    # TODO put all of this into one/two big loop(s)
    # Create empty Table
    backup_x = x
    backup_y = y
    ed_table = [[TableElement() for a in range(len(x)+1)] for b in range(len(y)+1)]

    # Fill table
    for j in range(len(y), -1, -1):
        for i in range(len(x), -1, -1):
            ed_table[i][j].stringX = x
            ed_table[i][j].stringY = y
            x = x[:-1]
        y = y[:-1]
        x = backup_x
    # Add the costs for every step:
    # --> every operation takes cost of 1 besides replace with the same character
    # Calculate the costs to the next 3 neighbored elements; only store costs if they are cheaper than already calculated
    ed_table[0][0].cost = 0
    # TODO insert an for loop with j
    for j in range(0, len(backup_y) +1):
        for i in range(0, len(backup_x) +1):
            # Compare to next "insert" element
            if i < len(backup_x):
                if ed_table[i+1][j].cost == -1 or ed_table[i+1][j].cost > (ed_table[i][j].cost + 1):
                    ed_table[i+1][j].cost = (ed_table[i][j].cost + 1)
            # Compare to next "delete" element
            if j < len(backup_y):
                if ed_table[i][j+1].cost == -1 or ed_table[i][j+1].cost > (ed_table[i][j].cost + 1):
                    ed_table[i][j+1].cost = (ed_table[i][j].cost + 1)
            # Compare to next "replace" element
            if i < len(backup_x) and j < len(backup_y):
                # Check if "replace" can be performed without changing a character
                if ed_table[i+1][j+1].stringX[-1:] == ed_table[i+1][j+1].stringY[-1:]:
                    ed_table[i+1][j+1].cost = ed_table[i][j].cost
                else:
                    ed_table[i + 1][j + 1].cost = ed_table[i][j].cost + 1
        if (j < len(backup_x)):
            ed_table[0][j+1].cost = ed_table[0][j].cost + 1

    # Find shortest Path through Table


    return ed_table[len(backup_x) - 1][len(backup_y) - 1].cost




class TableElement:

    def __init__(self):
        self.stringX = None
        self.stringY = None
        self.cost = -1


if __name__ == "__main__":
    # Read in two strings from command line.
    nr_args = len(sys.argv)
    if not nr_args == 3:
        raise Exception("script excepts two input strings")
    x = sys.argv[1]
    y = sys.argv[2]
    print("x = %s" % (x))
    print("y = %s" % (y))
    ed = compute_ed_recursively(x, y)
    print("Edit distance (x -> y): %i" % (ed))
