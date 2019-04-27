"""
Test cases for partition module
"""
import unittest
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList
from cracking_the_coding_interview.chapter2.problem4.partition import partition


class TestPartition(unittest.TestCase):

    def test_partition(self):
        # Create SinglyLinkedList
        sll = SinglyLinkedList()
        for i in [3, 5, 8, 5, 10, 2, 1]:
            sll.append(i)

        # Solution
        solution = SinglyLinkedList()
        for i in [3, 2, 1, 5, 8, 5, 10]:
            solution.append(i)

        # Check if partition produces the solution
        partition(sll, 5)
        self.assertEqual(solution, sll)

