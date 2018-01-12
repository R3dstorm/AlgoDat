#!/usr/bin/python3

import argparse
import numpy as np
import random
import time

class DynamicIntArray:
    """Dynamic integer array class implemented with fixed-size numpy array."""

    def __init__(self):
        """Create empty array with length 0 and capacity 1."""
        self._n = 0  # Number of elements in array
        self._c = 1  # Capacity
        self._a = self._create_array(self._c)

    def __len__(self):
        """Return number of elements in the array."""
        return self._n

    def __getitem__(self, i):
        """Return element at index i."""
        # Check for index out of bounds error.
        if not 0 <= i < self._n:
            raise IndexError('index out of bounds')
        return self._a[i]

    def append(self, value):
        """Add integer value to end of array."""
        resized = 0
        # Check if given value is of integer type.
        if not isinstance(value, int):
            raise TypeError('value is not integer')
        if self._n == self._c:  # time to resize
            self._resize(2 * self._c)
            resized = 1
        self._a[self._n] = value
        self._n += 1
        
        return resized


    def remove(self):
        """ Remove integer value at the end of array.

        :return: -
        """
        resized = 0
        if self._n <= self._c//3: # time to resize
            self._resize(self._c //2)
            resized = 1
        if(self._n > 0):
            self._n -= 1

        return resized

    def _resize(self, new_c):
        """Resize array to capacity new_c."""
        b = self._create_array(new_c)
        for i in range(self._n):
            b[i] = self._a[i]
        # Assign old array reference to new array.
        self._a = b
        self._c = new_c

    def _create_array(self, new_c):
        """Return new array with capacity new_c."""
        return np.empty(new_c, dtype=int)  # data type = integer

def test_case_1():
    ''' Implements a sequence of 10 million append operations starting with an empty array

    :return: none
    '''

    for i in range (0, 29):
        array1 = DynamicIntArray()
        input_size = 10**(i/4) #10**i
        start_time = time.clock()

        for i in range(0, int(input_size)):
            array1.append(random.randint(0, 1000000))
    
        print("%d \t %d" %(input_size, (time.clock()-start_time)*1000))

def test_case_2():
    ''' Implements a sequence of 10 million remove operations starting with an empty array

    :return: none
    '''

    for i in range (0, 29):
        array1 = DynamicIntArray()
        input_size = 10**(i/4)

        for i in range(0, int(input_size)):
            array1.append(random.randint(0, 1000000))
        
        start_time = time.clock()

        for i in range(0, int(input_size)):
            array1.remove()

        print("%d \t %d" % (input_size, (time.clock()-start_time)*1000))

def test_case_3():
    ''' Implements a sequence of 10 million operations starting with an array
        containing 1 million. The operations start with append and then alternate
        after each reallocation between append and remove

    :return: none
    '''

    for i in range (0, 29):
        array1 = DynamicIntArray()
        number_of_operations = 10**(i/4)
        append = 1

        for i in range(0, int(1e+6)):
            array1.append(random.randint(0, 1000000))

        start_time = time.clock()
        for i in range(0, int(number_of_operations)):
            # Change append/remove if reallocation occurs
            if append == 1:
                if array1.append(random.randint(0, 1000000)) == 1:
                    append = 0
            else:
                if array1.remove() == 1:
                    append = 1

        print("%d \t %d" % (number_of_operations, (time.clock()-start_time)*1000))

def test_case_4():
    ''' Implements a sequence of 10 million operations starting with an array
        containing 1 million. The operations start with remove and then alternate
        after each reallocation between remove and append

    :return: none
    '''

    for i in range(0, 29):
        array1 = DynamicIntArray()
        input_size = 10**(i/4)
        append = 0

        for i in range(0, int(1e+6)):
            array1.append(random.randint(0, 1000000))

        start_time = time.clock()
        for i in range(0, int(input_size)):
            # Change append/remove if reallocation occurs
            if append == 1:
                if array1.append(random.randint(0, 1000000)) == 1:
                    append = 0
            else:
                if array1.remove() == 1:
                    append = 1

        print("%d \t %d" % (input_size, (time.clock()-start_time)*1000))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= 'Output accumulated runtime for test cases using the dynamic int array.')
    parser.add_argument('--test', dest="test_case", type=int, default=1, help='number of testcase to run')

    parser.parse_args()
    args = parser.parse_args()
    if args.test_case == 1:
        test_case_1()
    if args.test_case == 2:
        test_case_2()
    if args.test_case == 3:
        test_case_3()
    if args.test_case == 4:
        test_case_4()
