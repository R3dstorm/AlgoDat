#! /usr/bin/python3


def heap_sort(array):
    """ sort list using the heap sort algorithm with max heap.

    test for complete heap with uneven number of elements
    >>> heap_sort([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19, 23, 27])
    [3, 4, 7, 8, 9, 10, 11, 12, 12, 14, 18, 19, 20, 23, 27]


    test for incomplete heap with even number of elements
    >>> heap_sort([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11])
    [3, 4, 7, 8, 9, 10, 11, 12, 12, 14, 18, 20]

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

    n = len(array)

    # First step is heapify for every layer of the heap starting from layer d-1
    heapify(array)

    # for all elements of heap
    while n > 0:
        # after heapify we take out the element with highest value
        # pick up last element of heap and place it at root
        array[n - 1], array[0] = array[0], array[n - 1]
        n -= 1

        # call repair_heap to restore max heap property
        repair_heap(array, 0, n)

    return array


def heapify(array):
    """ heapify data in given array to form a correct max heap.

    test for heapifying of array containing complete heap
    >>> heapify([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19, 23, 27])
    [27, 20, 23, 18, 12, 19, 12, 14, 4, 8, 7, 11, 9, 3, 10]


    test for heapifying of array containing incomplete heap
    >>> heapify([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19])
    [20, 18, 19, 14, 12, 11, 12, 10, 4, 8, 7, 3, 9]

    test for empty list
    >>> heapify([])
    []

    test for wrong datatype
    >>> heapify("blub")
    Traceback (most recent call last):
         ...
    TypeError: array must be a list

    :param array: holds the array containing the heap
    :param i:  index of parent node to heapify
    :return: array with node i heapified
    """

    # Check given given parameter data type.
    if not type(array) == list:
        raise TypeError('array must be a list')

    n = len(array)
    for i in range(n//2-1, -1, -1):
        repair_heap(array, i, n)

    return array


def repair_heap(array, start_index, heap_size):
    """ heapify the given node as root node with his consecutive children.
    The parent node is sifted until bottom layer.

    test for heapifying of single node with complete heap
    >>> repair_heap\
    ([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19, 23, 27], 0, 15)
    [12, 10, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19, 23, 27]


    test for incomplete heap with even number of elements
    >>> repair_heap([10, 12, 3, 4, 8, 9, 12, 14, 18, 20, 7, 11, 19], 2, 13)
    [10, 12, 12, 4, 8, 9, 3, 14, 18, 20, 7, 11, 19]

    test for empty list
    >>> repair_heap([], 0, 0)
    []

    test for wrong datatype
    >>> repair_heap("blub", 0, 5)
    Traceback (most recent call last):
         ...
    TypeError: array must be a list

    :param array: containing the heap plus organized
    :param start_index: index of root node to start heapifying at
    :param heap_size: rest size of heap contained in array
    :return: array heapified starting from start_index
    """

    # Check given given parameter data type.
    if not type(array) == list:
        raise TypeError('array must be a list')

    # Assume current node is max
    max_index = start_index
    left_child_index = 2*start_index+1
    right_child_index = 2*start_index+2

    # Check if left child node exists and has higher value than parent node
    if left_child_index < heap_size and \
            array[left_child_index] > array[max_index]:
        max_index = left_child_index

    # Check if right child node exists and has even higher value
    # than both parent and left child node
    if right_child_index < heap_size and \
            array[right_child_index] > array[max_index]:
        max_index = right_child_index

    # Swap values if root is not max
    if max_index != start_index:
        array[max_index], array[start_index] \
            = array[start_index], array[max_index]
        repair_heap(array, max_index, heap_size)

    return array


if __name__ == "__main__":
    # Create an unsorted list of integers.
    numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9, 12, 15, 17, 11, 166, 16, 2]
    # Sort the list.
    print(heap_sort(numbers))
