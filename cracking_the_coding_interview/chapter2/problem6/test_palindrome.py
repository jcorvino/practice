"""
Test cases for palindrome module
"""
import unittest
from cracking_the_coding_interview.chapter2.problem6.palindrome import palindrome
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        # Case 1: (1, 2, 3, 2, 1) = Palindrome (True)
        p = SinglyLinkedList()
        p.append(1)
        p.append(2)
        p.append(3)
        p.append(2)
        p.append(1)
        self.assertTrue(palindrome(p))

        # Case 2: (1) = Palindrome (True)
        p = SinglyLinkedList()
        p.append(1)
        self.assertTrue(palindrome(p))

        # Case 3: (9, 9) = Palindrome (True)
        p = SinglyLinkedList()
        p.append(9)
        p.append(9)
        self.assertTrue(palindrome(p))

        # Case 4: ('a', 'b', 'c', 'a') != Palindrome (False)
        p = SinglyLinkedList()
        p.append('a')
        p.append('b')
        p.append('c')
        p.append('a')
        self.assertTrue(palindrome(p))

        # Case 5 (empty case): () = Palindrome (True)
        self.assertTrue(palindrome(SinglyLinkedList()))
