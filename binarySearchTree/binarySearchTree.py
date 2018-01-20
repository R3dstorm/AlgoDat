#!/usr/bin/python3


class Node:
    """ Implements a single node of a linked list.
    """
    def __init__(self, key, element):
        """ Init for a single node of a linked list.
        >>> node = Node(2,5)
        Traceback (most recent call last):
            ...
        TypeError: element must be a string
        """
        if not type(key) == int:
            raise TypeError('key must be an integer')
        if not type(element) == str:
            raise TypeError('element must be a string')
        self.key = key
        self.element = element
        self.leftChild = None
        self.rightChild = None

    def to_string(self):
        """
        >>> node = Node(1,'"test"')
        >>> node.to_string()
        '(1, "test")'
        :return: string containing content of node
        """
        return '(' + str(self.key) + ', ' + self.element + ')'


class BinarySearchTree:
    """Implements the data structure and operations of a binary search tree:
    Rules:
        Search/Lookup:
            - Search the element with the given key.
            If no element is found return the element with the next (bigger) key.
        Insert:
            - We search for the key in our search tree
            - If a node is found we replace the value with the new one
            - Else we insert a new node at the corresponding None entry
    """

    def __init__(self):
        """Create empty list representing the binary search tree"""
        self._head = Node(None, None)
        self._last = self._head  # Is there a last element defined in a  BST with only one list?
        self._itemCount = 0

    def insert(self, insert_key, insert_element):
        insert_node = Node(insert_key, insert_element)

        # Check if list is empty
        if self.isEmpty():  # self._last == self._head:
            self._head.leftChild = insert_node

        else:
            # run through tree to find correct location
            current = self._head.leftChild
            inserted = False
            while inserted != True:  # so
                if insert_key < current.key:
                    if current.leftChild == None:
                        current.leftChild = insert_node
                        break;
                    else:
                        current = current.leftChild

                elif insert_key > current.key:
                    if current.rightChild == None:
                        current.rightChild = insert_node
                        break;
                    else:
                        current = current.rightChild

                else:  # Key is already inserted -> only change element
                    current.element = insert_element
                    return  # inserted = True # Alternative: return?
        self._itemCount += 1

    def lookup(self, search_key):
        ''' Put some Unittest here'''
        current = self._head.leftChild
        next_bigger = None

        while True:
            if search_key < current.key:
                if current.leftChild == None:
                    if (current.key < next_bigger.key):
                        return next_bigger.element
                    else:
                        return current.element
                else:
                    next_bigger = current
                    current = current.leftChild

            elif search_key > current.key:
                if current.rightChild == None:
                    return next_bigger.element
                else:
                    current = current.rightChild

            else:  # Key is already inserted -> return element
                return current.element

    def size(self):
        return self._itemCount

    def isEmpty(self):
        return self._itemCount == 0

    def to_string(self):
        '''
        '[(5, "five"), left: [(1, "one"), left: null, right: [(2, "two"), left: null, right: [(3, "three"), left: null, right: null]]], right: [(6, "six"), left: null, right: null]]'


        :return:
        '''
        if self.isEmpty():
            return 'null'
        else:
            current = self._head.leftChild
            output_string = ""
            output_string = self.to_string_slicing(current, output_string)
            return output_string

        while True:  # Break Condition:
            run = True
            while current.leftChild is not None:
                current = current.leftChild
                output_string += current.to_string()
                output_string += (', left: ')
            output_string += 'null'

            if current.leftChild == None and current.rightChild == None:
                break
            else:
                output_string.append(current.to_string())
                output_string.append(', left:')
                current = current.leftChild
                # output_string.append(current.to_string)

                # leftChild = current.leftChild.element # Für die Tonne... das klappt so nie!
                # rightChild = current.rightChild.element # Für die Tonne.... das klappt so nie!
                # output_string.append(print("(%d, ""%s""), left: %s, right %s" % current.key, current.element, leftChild, rightChild))

        return output_string

    def to_string_slicing(self, current, output_string):
        output_string += '[' + current.to_string()
        output_string += (', left: ')
        if (current.leftChild != None):
            #current = current.leftChild
            output_string = self.to_string_slicing(current.leftChild, output_string)

        else:
            output_string += ('null')
        output_string += (', right: ')
        if (current.rightChild != None):
            #current = current.rightChild
            output_string = self.to_string_slicing(current.rightChild, output_string)
        else:
            output_string += ('null')

        output_string += ']'
        return output_string


if __name__ == "__main__":
    searchTree = BinarySearchTree()
    searchTree.insert(5, '"five"')
    searchTree.insert(1, '"one"')
    searchTree.insert(2, '"two"')
    searchTree.insert(3, '"three"')
    searchTree.insert(6, '"six"')

    string = searchTree.to_string()
    searchTree.lookup(15)
