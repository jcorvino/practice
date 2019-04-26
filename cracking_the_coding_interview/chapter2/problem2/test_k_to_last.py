"""
Test cases for k_to_last module
"""
import unittest
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList
from cracking_the_coding_interview.chapter2.problem2.k_to_last import k_to_last


class TestKToLast(unittest.TestCase):

    def test_k_to_last(self):
        # Create SinglyLinkedList
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        sll.append(4)

        # Find last element
        data = k_to_last(sll, 1)
        self.assertEqual(data, 4)

        # Find 2nd to last element
        data = k_to_last(sll, 2)
        self.assertEqual(data, 3)

        # Find first element
        data = k_to_last(sll, 4)
        self.assertEqual(data, 1)

        # Check if it raises ValueError when k > len(sll)
        self.assertRaises(ValueError, k_to_last, sll, 10)

        # Check if it raises ValueError when k = 0
        self.assertRaises(ValueError, k_to_last, sll, 0)
