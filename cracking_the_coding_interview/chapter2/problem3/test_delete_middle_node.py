"""
Test cases for delete_middle_node module
"""
import unittest
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList
from cracking_the_coding_interview.chapter2.problem3.delete_middle_node import delete_middle_node


class TestDeleteMiddleNode(unittest.TestCase):

    def test_delete_middle_node(self):
        # Create SinglyLinkedList
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        sll.append(4)

        # Solution
        solution = SinglyLinkedList()
        solution.append(1)
        solution.append(3)
        solution.append(4)

        # Check if delete_middle_node produces the solution
        node = sll.head.next  # node 2
        delete_middle_node(sll, node)
        self.assertEqual(solution, sll)

