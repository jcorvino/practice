"""
Test cases for LinkedList module
"""
import unittest
from .node import Node
from .linkedlist import SinglyLinkedList, DoublyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.sll = SinglyLinkedList()
        self.linked_list_data = ['a', 'b', 'c', 'd', 2, True, ['sub', 'list'], False]
        for data in self.linked_list_data:  # Create singly linked list and populate w/ test data
            self.sll.append(data)

    def test_node(self):
        """
        Simple test cases for Node class
        """
        # Create node
        mynode = Node('test')

        # Test node
        self.assertEqual(mynode.data, 'test')
        self.assertIsNone(mynode.next)
        # self.assertIsNone(mynode.prev)

    def test_singly_linked_list_append(self):
        """
        Simple test cases for append method of SinglyLinkedList class
        """
        # Test if singly linked list was created correctly
        n = self.sll.head
        for data in self.linked_list_data:
            self.assertEqual(n.data, data)
            if n.next is None:
                self.end_node = n
            n = n.next

    def test_singly_linked_list_print(self):
        """
        Simple test cases for print method of SinglyLinkedList class
        """
        self.assertEqual(str(self.sll), 'SinglyLinkedList(' + ','.join([str(x) for x in self.linked_list_data]) + ')')
        # print(sll)

    def test_singly_linked_list_len(self):
        """
        Simple test cases for len method of SinglyLinkedList class
        """
        self.assertEqual(len(self.sll), 8)

    def test_singly_linked_list_remove(self):
        """
        Simple test cases for remove method of SinglyLinkedList class
        """
        # Test that the remove function does not raise errors
        while self.sll.head is not None:
            self.sll.remove(self.sll.head)
        self.sll.remove(Node('test'))  # No error should raise when node not found

