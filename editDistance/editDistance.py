#!/usr/bin/python3

import sys
import random
import time


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


class TableElement:
    def __init__(self):
        self.string_x = None
        self.string_y = None
        self.cost = -1


def compute_ed_via_table(x, y):
    """ Compute edit distance via dynamic programming table.

    >>> compute_ed_via_table("DINO", "GRAU")
    4
    >>> compute_ed_via_table("ABCDEFGHIJiuKLMNOPQRSTUVkl", "ABCDEFGHIJKLMNOjiPQRSTUVH")
    6
    >>> compute_ed_via_table("", "")
    0

    """
    # TODO put all of this into one/two big loop(s)
    # Create empty Table
    ed_table = [[TableElement() for a in range(len(y)+1)] for b in range(len(x)+1)]

    # Fill table
    # Last element should be enough for table
    for j in range(len(y), 0, -1):
        for i in range(len(x), 0, -1):
            ed_table[i][j].string_x = x[i - 1]
            ed_table[i][j].string_y = y[j - 1]

    # Add the costs for every step:
    # --> every operation takes cost of 1 besides replace with the same character
    # Calculate the costs to the next 3 neighbored elements;
    # Only store costs if they are cheaper than already calculated
    ed_table[0][0].cost = 0
    # TODO insert an for loop with j
    for j in range(0, len(y) + 1):
        for i in range(0, len(x) + 1):
            # Compare to next "insert" element
            if i < len(x):
                if ed_table[i+1][j].cost == -1 or ed_table[i+1][j].cost > (ed_table[i][j].cost + 1):
                    ed_table[i+1][j].cost = (ed_table[i][j].cost + 1)
            # Compare to next "delete" element
            if j < len(y):
                if ed_table[i][j+1].cost == -1 or ed_table[i][j+1].cost > (ed_table[i][j].cost + 1):
                    ed_table[i][j+1].cost = (ed_table[i][j].cost + 1)
            # Compare to next "replace" element
            if i < len(x) and j < len(y):
                # Check if "replace" can be performed without changing a character
                if ed_table[i+1][j+1].string_x == ed_table[i + 1][j + 1].string_y:
                    ed_table[i+1][j+1].cost = ed_table[i][j].cost
                else:
                    ed_table[i + 1][j + 1].cost = ed_table[i][j].cost + 1
        if j < len(y):
            ed_table[0][j+1].cost = ed_table[0][j].cost + 1

    # TODO Find shortest Path through Table and print operations

    return ed_table[len(x)][len(y)].cost


def compute_ed_via_table_master(x, y):
    """ Compute edit distance via dynamic programming table.

    >>> compute_ed_via_table("", "")
    0
    >>> compute_ed_via_table("chantalle", "schnalle")
    3
    >>> compute_ed_via_table("", "alda")
    4
    """
    m = len(x)
    n = len(y)
    # Initialize matrix as list of lists.
    matrix = [[0] * (n + 1) for i in range(m + 1)]
    # First add costs for empty word alignments.
    for i in range(0, m + 1):
        matrix[i][0] = i
    for j in range(0, n + 1):
        matrix[0][j] = j
    # Compute matrix.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i-1] != y[j-1]:
                delete_costs = matrix[i-1][j] + 1
                insert_costs = matrix[i][j-1] + 1
                replace_costs = matrix[i-1][j-1] + 1
                matrix[i][j] = min(delete_costs, insert_costs, replace_costs)
            else:
                matrix[i][j] = matrix[i-1][j-1]
    # Return last matrix entry = edit distance.
    return matrix[m][n]


def compute_max_common_range(x, y):
    """
    compute the maximum range of characters common in both strings.
    Routine checks every diagonal neighbored cell between the strings in the table
    :param x:
    :param y:
    :return:

    >>> compute_max_common_range("PFERDE", "APFEL")
    3
    """

    m = len(x)
    n = len(y)

    range_counter = 0
    max_range = 0

    for offset in range(-m, m):
        for yi in range(0, n):
            xi = offset + yi
            if 0 <= xi < m:
                if x[xi] != y[yi]:
                    range_counter = 0
                else:
                    range_counter += 1
                    max_range = max(range_counter, max_range)
    return max_range


def generate_random_numbers(n):
    return random.sample(range(1, n+1), n)


def print_runtime():
    for i in range(0, 10):
        random1 = generate_random_numbers(10**i)
        random2 = [x for x in random1]                  # Create copy of random 1
        random2[-1:] = "a"                              # Change Character
        start_time = time.time()
        ed = compute_ed_via_table(random1, random2)
        stop_time = time.time()
        print("%d \t %.5f %d" % ((10**i), stop_time - start_time, ed))


if __name__ == "__main__":
    # Read in two strings from command line.
    print_runtime()
    exit(0)
    nr_args = len(sys.argv)
    if not nr_args == 3:
        raise Exception("script excepts two input strings")
    x = sys.argv[1]
    y = sys.argv[2]
    print("x = %s" % x)
    print("y = %s" % y)
    ed = compute_ed_recursively(x, y)
    print("Edit distance (x -> y): %i" % ed)
