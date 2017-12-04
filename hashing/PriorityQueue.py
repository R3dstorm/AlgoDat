#!/usr/bin/python3

class PriorityQueueItem:
    """ Provides a handle for a queue item.
    A simple class implementing a key-value pair,
    where the key is an integer, and the value can
    be an arbitrary object. Index is the heap array
    index of the item.
    """

    def __init__(self, key, value, index):
        self._key = key
        self._value = value
        self._index = index

    def __lt__(self, other):
        """ Enables us to compare two items with a < b.
        The __lt__ method defines the behavior of the
        < (less than) operator when applied to two
        objects of this class. When using the code a < b,
        a.__lt__(b) gets evaluated.
        There are many other such special methods in Python.
        See "python operator overloading" for more details.
        """
        return self._key < other._key

    def get_heap_index(self):
        """ Return heap index of item."""
        return self._index

    def set_heap_index(self, index):
        """ Update heap index of item."""
        self._index = index

    def change_key(self, key):
        ''' Change the key of the object'''
        self._key = key


class PriorityQueueMinHeap:
    """Priority queue implemented as min heap."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._list = []

    def insert(self, key, value):
        '''return inserted item object
        >>> k = [(8, 'T', 0), (15, 'E', 1), (16, 'S', 2), (17, 'T', 3), (22, '2', 4), (19, '1', 5)]
        >>> k = PriorityQueueMinHeap()
        >>> k.insert (23,'3')
        >>> k.insert (22,'4')
        >>> k.insert (21,'5')
        >>> k.insert (20,'6')
        >>> k.get_min()
        (23,'3')
        '''

        inserted_item_object = PriorityQueueItem(key, value, len(self._list))
        self._list.append(inserted_item_object)
        self._repair_heap_up(len(self._list)-1)

        return inserted_item_object

    def get_min(self):
        ''' return the object with the smallest key
        >>> k = PriorityQueueMinHeap()
        >>> k.insert (23,'3')
        >>> k.insert (22,'4')
        >>> k.insert (21,'5')
        >>> k.insert (20,'6')
        >>> k.get_min()
        'PriorityQueueItem(20, '6', 0)'
        '''
        # Check for empty list
        if not self._list:
            return

        else:
            return self._list[0]

    def delete_min(self):
        ''' Delete the element with lowest key (first in heap)

        >>> k = PriorityQueueMinHeap()
        >>> k.insert (23,'3')
        >>> k.insert (22,'4')
        >>> k.insert (21,'5')
        >>> k.insert (20,'6')
        >>> k.delete_min()
        >>> k.get_min()
        'PriorityQueueItem(21, '5', 0)'
        '''

        # Swap last element with first element and delete the last element
        self._swap_items(0,(len(self._list)-1))
        del self._list[len(self._list)-1]
        self._repair_heap_down(0)

    def change_key(self, item, new_key):
        ''' Change the key of an item and resort the heap

        :param item: item to change the key for
        :param new_key: the new key applied to the given item

        >>> k = PriorityQueueMinHeap()
        >>> k_item_1 = k.insert (23,'3')
        >>> k_item_2 = k.insert (22,'4')
        >>> k_item_3 = k.insert (21,'5')
        >>> k_item_4 = k.insert (20,'6')
        >>> k.change_key(k_item_4, 35)
        'PriorityQueueItem(21, '5', 0)'
        '''

        # Change the key of the element
        self._list[item.get_heap_index()].change_key(new_key)
        # Check direction of heap violation
        i = item.get_heap_index()
        parent_node = int((i - 1) / 2)
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if i != 0:
            if self._list[parent_node] > self._list[i]:
                self._repair_heap_up(i)
                return

        if right_child_index < (len(self._list)) and \
                self._list[right_child_index] < self._list[i]:
            self._repair_heap_down(i)

        elif right_child_index < (len(self._list)) and \
                self._list[left_child_index] < self._list[i]:
            self._repair_heap_down(i)



    def size(self):
        ''' returns the current size of the queue

        :return: the size of the queue

        >>> k = PriorityQueueMinHeap()
        >>> k_item_1 = k.insert (23,'3')
        >>> k_item_2 = k.insert (22,'4')
        >>> k_item_3 = k.insert (21,'5')
        >>> k_item_4 = k.insert (20,'6')
        >>> k.size()
        4
        '''

        return len(self._list)

    def _repair_heap_up(self, violated_position):
        #Repair the heap contained in _list from given position upwards

        if violated_position != 0:
            i = violated_position
            parent_node = int((i - 1) / 2)
            if self._list[parent_node] > self._list[i]:
                self._swap_items(parent_node, i)
                self._repair_heap_up(parent_node)

    def _repair_heap_down(self, violated_position):
        #Repair the heap contained in _list from given position downwards

        # Assume current node is min
        heap_size = len(self._list)
        min_index = violated_position
        left_child_index = 2 * violated_position + 1
        right_child_index = 2 * violated_position + 2

        # Check if left child node exists and has higher value than parent node
        if left_child_index < heap_size and \
                self._list[left_child_index] < self._list[min_index]:
            min_index = left_child_index

        # Check if right child node exists and has even higher value
        # than both parent and left child node
        if right_child_index < heap_size and \
                self._list[right_child_index] < self._list[min_index]:
            min_index = right_child_index

        # Swap values if root is not max
        if min_index != violated_position:
            self._swap_items(min_index,violated_position)
            self._repair_heap_down(min_index)




    def _swap_items(self, i, j):
        # Swap items with indices i,j (also swap their indices!)
        store_j = self._list[j].get_heap_index()
        store_i = self._list[i].get_heap_index()
        self._list[i].set_heap_index(store_j)
        self._list[j].set_heap_index(store_i)
        self._list[i], self._list[j] = self._list[j], self._list[i]


if __name__ == "__main__":
    # Create priority queue object.
    pq1 = PriorityQueueMinHeap()
    # Insert some flights into queue.
    pq1_item1 = pq1.insert(1, "Airforce One")
    pq1_item2 = pq1.insert(45, "Bermuda Triangle Blues (Flight 45)")
    pq1_item3 = pq1.insert(666, "Flight 666")
    # ....

