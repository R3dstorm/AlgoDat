#! /usr/bin/python3


# ToDo: Change heapify (array, i) to heapify (array)-> using repair_heap

import math

def heap_sort (array):
    """ sort list using the heap sort algorithm with max heap.
    test for complete heap with uneven number of elements
    >>> heap_sort([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19, 23, 27])
    [27, 20, 23, 18, 12, 19, 12, 14, 4, 8, 7, 11, 9, 3, 10]


    # test for incomplete heap with even number of elements
    # >>> heap_sort([@todo])
    # [@TODO]

    test for empty list
    >>> heap_sort([])
    []

    test for wrong datatype
    >>> heap_sort("blub")
    Traceback (most recent call last):
         ...
    TypeError: array must be a list

    :param array: holds a list of unsorted values
    :return: sorted list
    """

    # Check given given parameter data type.
    if not type(array) == list:
        raise TypeError('array must be a list')

    # First step is heapify for every layer of the heap starting from layer d-1
    n = len(array)
    for i in range (n//2-1, -1, -1):
        heapify(array, i)

    # for all elements of heap
    while n >= 0:
        # after heapify we take out the element with highest value
        # pick up last element of heap and place it at root
        array[n - 1], array[0] = array[0], array[n - 1]

        # call repair_heap to restore max heap property
        repair_heap(array, 0, n)
        n -= 1

    return array


def heapify (array, i):
    """ heapify the given node as parent with his children.
    The parent node is sifted until bottom layer.

    test for heapifying of single node with complete heap
    >>> heapify([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19, 23, 27], 0)
    [12, 10, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19, 23, 27]


    test for incomplete heap with even number of elements
    >>> heapify([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19], 2)
    [10, 12, 12, 4, 8, 9, 3, 14, 18, 20, 7, 11, 19]

    test for empty list
    >>> heapify([],0)
    []

    test for wrong datatype
    >>> heap_sort("blub")
    Traceback (most recent call last):
         ...
    TypeError: array must be a list

    :param array: holds the array containing the heap
    :param i:  index of parent node to heapify
    :return: array with node i heapified
    """

    # Assume current node is max
    max_index           = i
    left_child_index    = 2*i+1
    right_child_index   = 2*i+2

    # Check if left child node exists and has higher value than parent node
    if left_child_index < len(array) and array[left_child_index] > array[max_index]:
        max_index = left_child_index

    # Check if right child node exists and has even higher value than both parent and left child node
    if right_child_index < len(array) and array[right_child_index] > array[max_index]:
        max_index = right_child_index

    # Swap values if root is not max
    if max_index != i:
        array[max_index], array[i] = array[i], array [max_index]
        heapify(array, max_index)

    #
    # # Get length of the list.
    # n = len(array)
    #
    # # Get depth of heap
    # d = math.log2(n - 1)
    #
    # # Check every layer of the heap starting with bottom
    # for i in range(1, d -1): # shall count from d to 1
    #     # find index of first note in last layer
    #     index_node1 = i
    #     index_node2 = i+1
    #     index_root = i-(math.pow(2, i-1)) #index_node - number of nodes in layer of root node
    #     if index_#root correct?


    return array


def repair_heap(array, start_index, heap_size):

    return array

if __name__ == "__main__":
    # Create an unsorted list of integers.
    numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
    # Sort the list.
    print(heap_sort(numbers))