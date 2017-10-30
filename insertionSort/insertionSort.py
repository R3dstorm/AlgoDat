#! /usr/bin/python3


def insertionSort(lst):
    """ sort list using the InsertionSort algorithm.

    test for uneven number of bytes
    >>> insertionSort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    test for even number of bytes
    >>> insertionSort([10, 55, 90, 110, 10, 2])
    [2, 10, 10, 55, 90, 110]

    test for empty list
    >>> insertionSort([])
    []

    test for wrong datatype
    >>> insertionSort("blub")
    Traceback (most recent call last):
        ...
    TypeError: lst must be a list

    :param lst: holds a list of unsorted values
    :return: sorted list
    """

    # Check given given parameter data type.
    if not type(lst) == list:
        raise TypeError('lst must be a list')

    # Get length of the list.
    n = len(lst)
    # For each list element.
    for i in range(1, n):   # @coder try later: for i in lst
        # Check the next value in list[i...n-1].
        if lst[i] < lst[i-1]:

            # Next element is smaller than current one
            smallerElement = lst[i]

            # find correct position
            for j in range(i):
                if smallerElement <= lst[j]:
                    insertIndex = j
                    break

            # reallocate upper data
            counter = 0
            for j in range(insertIndex, i):
                lst[i-counter] = lst[i-counter-1]
                counter += 1
            # insert data element
            lst[insertIndex] = smallerElement
        # leave rest

    return lst


if __name__ == "__main__":
    # create an unsorted list of integers.
    numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
    # sort the list.
    print(insertionSort(numbers))
