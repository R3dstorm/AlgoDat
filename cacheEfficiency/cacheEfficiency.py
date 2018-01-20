#!/usr/bin/python3

import random
import time
import sys
import argparse

# Class handling hash table
class HashTable:

    def __init__(self,p,m):
        self._buckets = [[]for i in range(m)]
        self._m = m
        self._p = p
        self._a = random.randint(1, self._p - 1)
        self._b = random.randint(0, self._p - 1)

    # Insert a new element into the hash list
    def insert_element(self, key, value):
        bucket = ((self._a * key + self._b) % self._p) %self._m

        for i in range(len(self._buckets[bucket])):
            entry = self._buckets[bucket][i]

            if entry[0] == key:  # Entry already exists
                self._buckets[bucket][i] = (key,value)
                break
        # If key is non existing add it to the bucket
        self._buckets[bucket].append((key, value))


def quicksort(l, start, end):
    if (end - start) < 1:
        return

    i = start
    k = end
    piv = l[start]

    while k > i:
        while l[i] <= piv and i <= end and k > i:
            i += 1
        while l[k] > piv and k >= start and k >= i:
            k -= 1

        if k > i:  # Swap elements
            (l[i], l[k]) = (l[k], l[i])

    (l[start], l[k]) = (l[k], l[start])
    quicksort(l, start, k - 1)
    quicksort(l, k + 1, end)


def generate_random_numbers(n):
    return [random.randint(0,n) for a in range(0,n)]


def measure_runtime(n):
    # Runtime of Function A
    time_diff_A = 0
    time_diff_B = 0
    for i in range(0, 3):
        random_numbers = generate_random_numbers(n)
        start_time = time.clock()
        quicksort(random_numbers, 0, len(random_numbers)-1)
        time_diff_A += (time.clock()-start_time)*1000

    # Runtime of Function B
    for i in range(0, 3):
        random_numbers = generate_random_numbers(n)
        hash_map = HashTable((2 ** 31) - 1, 2 ** 15)
        start_time = time.clock()
        for i in range(n):
            hash_map.insert_element(i,random_numbers[i])
        time_diff_B += (time.clock()-start_time)*1000

    return (time_diff_A / 3), (time_diff_B / 3)


def setup_argument_parser():
    """Setup argparse parser."""
    help_description = """
    This program implements both a sorting algorithm
    and a hash table. The runtime can be output in 
    different ways:
    
    -table: generates an table containing runtimes
    for input size from n¹⁷ to n²².
    """

    # Define argument parser.
    p = argparse.ArgumentParser(add_help=False,
                                prog="cacheEfficiency.py",
                                usage="%(prog)s -table",
                                description=help_description,
                                formatter_class=argparse.RawTextHelpFormatter)
    # Define an argument group.
    parse_group_args = p.add_argument_group("Arguments")
    # Define arguments.
    parse_group_args.add_argument("-h", "--help",
                                  action="help",
                                  help="Print help message")
    parse_group_args.add_argument("-table",
                                  dest="table",
                                  type= bool,
                                  help="enable table output",
                                  required=False)
    parse_group_args.add_argument("-a",
                                  dest="algorithm",
                                  type=str,
                                  default="A",
                                  help="algorithm to print table for",
                                  required=False)
    return p

if __name__ == "__main__":
    # Setup argparse and define available command line arguments.
    parser = setup_argument_parser()
    # Read the command line arguments.
    args = parser.parse_args()

    # Call function
    for i in range(15, 23):
        runtime = measure_runtime(2**i)
        if args.table == False:
            print ("Runtime for A is: %d \n"
                   "Runtime for B is: %d \n"
                   % (runtime[0], runtime[1]))
        else:
            if args.algorithm == "A":
                print("%d \t %d" %(2**i, runtime[0]))
            elif args.algorithm == "B":
                print("%d \t %d" %(2**i, runtime[1]))

