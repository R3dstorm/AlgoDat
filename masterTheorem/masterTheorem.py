#!/usr/bin/python3

import random
from math import log


def runtime_function(n, start, end):
    """ implements a recursive function achieving runtime
    T(n) = 4T(n/2) + n²
    Function resolves data into 4 substeps every recursion que, operating half the data"""

    if (end - start) < 1:
        return

    # Solve sub problem
    size = end - start
    for i in range (size):         # Runtime of O(n)
        m = start + (end - start)//2
        for k in range (size):     # Runtime of O(n)
            n[k] += 1   # Simple Operation O(1)

    runtime_function(n, start, m)
    runtime_function(n, m+1, end)
    runtime_function(n, start, m)
    runtime_function(n, m+1, end)


def calc_runtime (n):

    if n <= 1:
        return 1

    return 4 * calc_runtime(n // 2) + n ** 2

if __name__ == "__main__":
    n = [random.randint(0,10) for a in range(0, 10)]


    # Print a csv header with 'tab' as separator
    print("n\tmin\tf\tmax")

    for n in range (1, int(10e+8), int(10e+5)):
        result = calc_runtime(n)
        print("%d \t %d \t %d \t %d" % (n, 1 * (n ** 2) * log(n), result, 2 * (n ** 2) * log(n)))
    # runtime_function(n, 0, len(n))
