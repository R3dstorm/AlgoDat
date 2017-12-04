#! /usr/bin/python3


import random


class HashFunction:
    ''' New Class'''
    a = 0
    b = 0
    p = 0
    u = 0
    m = 0

    def __init__(self):
        '''init class'''
        self.a = 1 # Parameter a
        self.b = 1 # Parameter b
        self.p = 101 # Prime number
        self.u = 100 # Universe size
        self.m = 100 # Hash table size

    def apply(self, x):
        '''apply hash function to a given key value
        and return hash table index

        :param x: given key value
        :return: index of hash table
        '''

        hash_table_index = ((self.a * x + self.b) % self.p) % self.m

        return hash_table_index

    def set_random_parameters(self):
        '''sets random parameters for a and b'''
        self.a = random.randint(1, self.p)
        self.b = random.randint(0, self.p)


def mean_bucket_size(s, h):
    ''' gets a list of keys and a hash function object
    and returns the calculated mean bucket size'''

    # buckets only contains the indices
    buckets = [0] * h.m
    empty_bucket_counter = 0

    size = len(s)
    for i in range(0,size):
        buckets[(h.apply(s[i]))] +=1
    #count empty buckets
    for i in range(0,h.m):
        if (buckets[i] == 0):
            empty_bucket_counter +=1

    return size/(h.m-empty_bucket_counter)


def estimate_c_for_single_set(s, h):
    ''' Given a set of keys S, the method
        calculates the mean bucket size for 1000 random
        hash functions and from this calculates the value
        of c and returns c

    :param s: set of keys
    :param h: hash function used
    :return: lowest mean_bucket size
    '''
    c = 0
    c_min = 1000000
    amount_of_keys = len(s)

    for i in range(0,1000):
        h.set_random_parameters()
        mean_size = mean_bucket_size(s,h)
        c = (mean_size -1) * h.m / amount_of_keys
        if (c < c_min):
            c_min = c

    return c_min


class CcValues:
    c_mean = 0
    c_min = 0
    c_max = 0

    def __init__(self):
        self.c_max = 0
        self.c_mean = 0
        self.c_min = 1000000


def estimate_c_for_multiple_sets(n, k, h):
    ''' Generates random key sets and calculates for each
        of the key sets the best possible c

    :param n: number of key sets to generate
    :param k: size of key sets to generate
    :param h: hash object to use
    :return:
    '''

    result = CcValues()

    for i in range (0,n):
        # Generate Key set
        key_set = create_random_universe_subset(k,h.u)
        c = estimate_c_for_single_set(key_set,h)
        result.c_mean += c
        if c > result.c_max:
            result.c_max = c
        if c < result.c_min:
            result.c_min = c

    result.c_mean /= n
    return result


def create_random_universe_subset(k, u):
    '''
    generates a list of random unique keys with size k, including
    numbers of the universe u
    :param k: size of key list
    :param u: max number of universe
    :return: list of random generated keys
    '''

    key_list = []
    if u >= k: # Check if universe has enough numbers to find unique keys
        while len(key_list) < k:
            random_key = int(random.random() * u)
            if not random_key in key_list:
                key_list.append(random_key)
    return key_list


if __name__ == '__main__':

    h = HashFunction()
    h.p = 101
    c_results = estimate_c_for_multiple_sets(1000,20,h)
    print ("For running with p=101 the result is:\n"
           "mean of c: %f\n"
           "max of c: %f\n"
           "min of c: %f\n" % (c_results.c_mean,
                               c_results.c_max,
                               c_results.c_min))
    h.p = 10
    c_results = estimate_c_for_multiple_sets(1000,20,h)
    print ("For running with p=10 the result is:\n"
           "mean of c: %f\n"
           "max of c: %f\n"
           "min of c: %f\n" % (c_results.c_mean,
                               c_results.c_max,
                               c_results.c_min))