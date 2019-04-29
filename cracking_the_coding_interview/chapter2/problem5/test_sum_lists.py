"""
cases for sum_lists module
"""
import unittest
from cracking_the_coding_interview.chapter2.problem5.sum_lists import sum_lists_reverse, sum_lists_forward, pad_linked_list
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList


class TestSumLists(unittest.TestCase):

    def test_pad_linked_list(self):
        a = SinglyLinkedList()
        a.append(15)

        solution = SinglyLinkedList()
        solution.append(0)
        solution.append(0)
        solution.append(15)

        pad_linked_list(a, 2)
        self.assertEqual(a, solution)

    def test_sum_lists_reverse(self):
        # Case 1: 617 + 295 = 912
        a = SinglyLinkedList()
        a.append(7)
        a.append(1)
        a.append(6)

        b = SinglyLinkedList()
        b.append(5)
        b.append(9)
        b.append(2)

        solution = SinglyLinkedList()
        solution.append(2)
        solution.append(1)
        solution.append(9)

        out = sum_lists_reverse(a, b)
        self.assertEqual(out, solution)

        # Case 2: 617 + 29 + 3 = 649
        a = SinglyLinkedList()
        a.append(7)
        a.append(1)
        a.append(6)

        b = SinglyLinkedList()
        b.append(9)
        b.append(2)

        c = SinglyLinkedList()
        c.append(3)

        solution = SinglyLinkedList()
        solution.append(9)
        solution.append(4)
        solution.append(6)

        out = sum_lists_reverse(a, b, c)
        self.assertEqual(out, solution)

        # Case 3: 8 + 8 = 16
        a = SinglyLinkedList()
        a.append(8)

        b = SinglyLinkedList()
        b.append(8)

        solution = SinglyLinkedList()
        solution.append(6)
        solution.append(1)

        out = sum_lists_reverse(a, b)
        self.assertEqual(out, solution)

    def test_sum_lists_forward(self):
        # Case 1: 617 + 295 = 912
        a = SinglyLinkedList()
        a.append(6)
        a.append(1)
        a.append(7)

        b = SinglyLinkedList()
        b.append(2)
        b.append(9)
        b.append(5)

        solution = SinglyLinkedList()
        solution.append(9)
        solution.append(1)
        solution.append(2)

        out = sum_lists_forward(a, b)
        self.assertEqual(out, solution)

        # Case 2: 917 + 99 + 3 = 1019
        a = SinglyLinkedList()
        a.append(9)
        a.append(1)
        a.append(7)

        b = SinglyLinkedList()
        b.append(9)
        b.append(9)

        c = SinglyLinkedList()
        c.append(3)

        solution = SinglyLinkedList()
        solution.append(1)
        solution.append(0)
        solution.append(1)
        solution.append(9)

        out = sum_lists_forward(a, b, c)
        self.assertEqual(out, solution)


