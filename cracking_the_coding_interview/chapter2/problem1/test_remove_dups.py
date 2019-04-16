"""
Test cases for remove_dups module
"""
import unittest
import copy
# from cracking_the_coding_interview.chapter2.linkedlist.node import Node
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList, DoublyLinkedList
from .remove_dups import remove_dups


class TestRemoveDups(unittest.TestCase):

    def setUp(self):
        # SinglyLinkedList with duplicates
        self.sll_with_duplicates = SinglyLinkedList()
        self.linked_list_data = [1, 1, 2, 3, 2, 3, ['abc'], ['abc']]
        for data in self.linked_list_data:
            self.sll_with_duplicates.append(data)

        # Solution (duplicates removed)
        self.sll_solution = SinglyLinkedList()
        self.linked_list_solution_data = [1, 2, 3, ['abc']]
        for data in self.linked_list_solution_data:
            self.sll_solution.append(data)

    def test_remove_dups(self):
        self.assertNotEqual(self.sll_with_duplicates, self.sll_solution)
        remove_dups(self.sll_with_duplicates)
        self.assertEqual(self.sll_with_duplicates, self.sll_solution)
