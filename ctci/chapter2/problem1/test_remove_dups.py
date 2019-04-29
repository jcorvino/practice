"""
Test cases for remove_dups module
"""
import unittest
import copy
# from ctci.chapter2.linkedlist.node import Node
from ctci.chapter2.linkedlist.linkedlist import SinglyLinkedList, DoublyLinkedList
from ctci.chapter2.problem1.remove_dups import remove_dups, remove_dups_hashable


class TestRemoveDups(unittest.TestCase):

    def setUp(self):
        # setUp for remove_dups:
        #
        # SinglyLinkedList with duplicates
        self.sll = SinglyLinkedList()
        linked_list_data = [1, 1, 2, 3, 2, 3, ['abc'], ['abc']]
        for data in linked_list_data:
            self.sll.append(data)

        # Solution (duplicates removed)
        self.sll_solution = SinglyLinkedList()  # solution for non-hashable case
        linked_list_solution_data = [1, 2, 3, ['abc']]
        for data in linked_list_solution_data:
            self.sll_solution.append(data)

        # setUp for remove_dups_hashable:
        #
        # SinglyLinkedList with hashable data
        self.sll_hashable = SinglyLinkedList()
        hashable_linked_list_data = [1, 1, 2, 3, 2, 3, ('abc', 'def'), ('abc', 'def')]
        for data in hashable_linked_list_data:
            self.sll_hashable.append(data)

        # Hashable solution (duplicates removed)
        self.sll_hashable_solution = SinglyLinkedList()  # solution for non-hashable case
        linked_list_solution_data = [1, 2, 3, ('abc', 'def')]
        for data in linked_list_solution_data:
            self.sll_hashable_solution.append(data)

    def test_remove_dups(self):
        # Test remove_dups function
        self.assertNotEqual(self.sll, self.sll_solution)
        remove_dups(self.sll)
        self.assertEqual(self.sll, self.sll_solution)

    def test_remove_dups_hashable(self):
        # Test remove_dups hashable function
        # Requires hashable data
        self.assertNotEqual(self.sll_hashable, self.sll_hashable_solution)
        remove_dups_hashable(self.sll_hashable)
        self.assertEqual(self.sll_hashable, self.sll_hashable_solution)
