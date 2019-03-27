"""
Test cases for LinkedList module
"""
import unittest
from .Node import Node
from cracking_the_coding_interview.chapter2.linkedlist import SinglyLinkedList, DoublyLinkedList



class TestLinkedList(unittest.TestCase):

    def test_node(self):
        """
        Simple test cases for Node class
        """
        # Create node
        mynode = Node('test')

        # Test node
        self.assertEqual(mynode.data, 'test')
        self.assertIsNone(mynode.next)
        self.assertIsNone(mynode.prev)

    def test_singly_linked_list(self):
        """
        Simple test cases for SinglyLinkedList class
        """
        # Create singly linked list and populate w/ test data
        sll = SinglyLinkedList()
        linked_list_data = ['a', 'b', 'c', 'd', 2, True, ['sub', 'list'], False]
        for data in linked_list_data:
            sll.append(data)

        # Test if singly linked list was created correctly
        n = sll.head
        for data in linked_list_data:
            self.assertEqual(n.data, data)
            if n.next is None:
                end_node = n
            n = n.next

        # Test that the remove function does not raise errors
        sll.remove(end_node)
        while sll.head is not None:
            sll.remove(sll.head)
        sll.remove(Node('test'))  # No error should raise when node not found

    def test_doubly_linked_list(self):
        """
        Simple test cases for DoublyLinkedList class
        """
        pass
