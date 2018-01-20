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
        if (not type(key) == int) and (not key is None):
            raise TypeError('key must be an integer')
        if (not type(element) == str) and (not element is None):
            raise TypeError('element must be a string')
        self.key = key
        self.element = element
        self.leftChild = None
        self.rightChild = None

    def to_string(self):
        """ converts the nodes data (key and element data) into a string
        :return: string containing content of node.
        >>> node = Node(1,'"test"')
        >>> node.to_string()
        '(1, "test")'
        """
        return '(' + str(self.key) + ', ' + self.element + ')'


class BinarySearchTree:
    """ Implements the data structure and operations of a binary search tree:
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
        """ Create empty list representing the binary search tree data."""
        self._head = Node(None, None)
        self._last = self._head  # Is there a last element defined in a  BST with only one list?
        self._itemCount = 0

    def insert(self, insert_key, insert_element):
        """ Inserts a new node at the correct position in the tree.
        :param insert_key: key of the new inserted node
        :param insert_element: element data of the new inserted node
        >>> searchTree = BinarySearchTree()
        >>> searchTree.insert(1, '"red"')
        >>> searchTree.insert(4, '"blue"')
        >>> searchTree.to_string()
        '[(1, "red"), left: null, right: [(4, "blue"), left: null, right: null]]'
        """
        insert_node = Node(insert_key, insert_element)
        # Check if list is empty
        if self.is_empty():  # self._last == self._head:
            self._head.leftChild = insert_node
        else:
            # run through tree to find correct location
            current = self._head.leftChild
            inserted = False
            while not inserted:
                if insert_key < current.key:
                    if current.leftChild is None:
                        current.leftChild = insert_node
                        break;
                    else:
                        current = current.leftChild

                elif insert_key > current.key:
                    if current.rightChild is None:
                        current.rightChild = insert_node
                        break;
                    else:
                        current = current.rightChild

                else:  # Key is already inserted -> only change element
                    current.element = insert_element
                    return
        self._itemCount += 1

    def lookup(self, search_key):
        """Serach for given key. Return element with next bigger key if key is not found or reutrn "not found" if key is not found and there is no element with a bigger key.

        :param search_key: search for element with this key
        :return: element with this key or with next bigger key
        >>> searchTree = BinarySearchTree()
        >>> searchTree.insert(1, '"red"')
        >>> searchTree.insert(4, '"blue"')
        >>> searchTree.insert(3, '"yellow"')
        >>> searchTree.lookup(1)
        '"red"'
        >>> searchTree.lookup(3)
        '"yellow"'
        >>> searchTree.lookup(5)
        '"not found"'
        >>> searchTree.lookup(2)
        '"yellow"'
        >>> searchTree1 = BinarySearchTree()
        >>> searchTree1.insert(12, '"twelve"')
        >>> searchTree1.insert(7, '"seven"')
        >>> searchTree1.insert(14, '"fourteen"')
        >>> searchTree1.insert(18, '"eighteen"')
        >>> searchTree1.insert(16, '"sixteen"')
        >>> searchTree1.insert(3, '"three"')
        >>> searchTree1.insert(5, '"five"')
        >>> searchTree1.insert(10, '"ten"')
        >>> searchTree1.insert(15, '"fifteen"')
        >>> searchTree1.lookup(14)
        '"fourteen"'
        >>> searchTree1.lookup(6)
        '"seven"'
        >>> searchTree1.lookup(4)
        '"five"'
        >>> searchTree.lookup(19)
        '"not found"'
        """

        current = self._head.leftChild
        next_bigger = None
        while True:
            if search_key < current.key:
                next_bigger = current
                if current.leftChild is None:
                    return next_bigger.element
                else:
                    current = current.leftChild
            elif search_key > current.key:
                if current.rightChild is None:
                    if next_bigger is not None:
                        return next_bigger.element
                    else:
                        return '"not found"'
                else:
                    current = current.rightChild
            else:  # Key is already inserted -> return element
                return current.element

    def size(self):
        """ Returns the current size of the tree in number of nodes
        :return: number of nodes in tree
        >>> searchTree = BinarySearchTree()
        >>> searchTree.size()
        0
        >>> searchTree.insert(1, '"red"')
        >>> searchTree.insert(4, '"blue"')
        >>> searchTree.insert(3, '"yellow"')
        >>> searchTree.size()
        3
        """

        return self._itemCount

    def is_empty(self):
        """ Returns if the tree is empty (=true)
        :return: =true for empty tree
        >>> searchTree = BinarySearchTree()
        >>> searchTree.is_empty()
        True
        >>> searchTree.insert(1, '"red"')
        >>> searchTree.is_empty()
        False
        """

        return self._itemCount == 0

    def to_string(self):
        """ Returns a string of the given tree containing all elements of the tree, recursively starting with left branch
        :return: string containing all elements of the tree
        >>> searchTree = BinarySearchTree()
        >>> searchTree.to_string()
        'null'
        >>> searchTree.insert(1, '"red"')
        >>> searchTree.insert(4, '"blue"')
        >>> searchTree.to_string()
        '[(1, "red"), left: null, right: [(4, "blue"), left: null, right: null]]'
        """

        if self.is_empty():
            return 'null'
        else:
            current = self._head.leftChild
            output_string = ""
            output_string = self.to_string_slicing(current, output_string)
            return output_string

    def to_string_slicing(self, current, output_string):
        """ Helper function for "to_string" to implement the recursion on the tree elements

        :param current: current node of the tree (call with first node)
        :param output_string: empty string used by function to accumulate output
        :return: string containing accumulated content of tree
        -> Test of "to_string" involves "to_string_slicing"
        """
        output_string += '[' + current.to_string()
        output_string += (', left: ')
        if (current.leftChild is not None):
            #current = current.leftChild
            output_string = self.to_string_slicing(current.leftChild, output_string)

        else:
            output_string += ('null')
        output_string += (', right: ')
        if (current.rightChild is not None):
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
    string = searchTree.lookup(15)

    test = 1
