"""
cases for sum_lists module
"""
import unittest
from cracking_the_coding_interview.chapter2.problem5.sum_lists import sum_lists_reverse
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList


class TestSumLists(unittest.TestCase):

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


