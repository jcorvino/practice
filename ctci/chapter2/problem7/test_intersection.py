"""
Test cases for intersection module
"""
import unittest
from ctci.chapter2.problem7.intersection import intersection, intersection_fast
from ctci.chapter2.linkedlist.linkedlist import SinglyLinkedList
from ctci.chapter2.linkedlist.node import Node


class TestIntersection(unittest.TestCase):
    
    def setUp(self):
        # Case without intersection
        self.a = SinglyLinkedList()
        self.b = SinglyLinkedList()
        self.b.append(1)
        self.b.append(2)

        # Case with intersection
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n1.next = self.n2

        self.c = SinglyLinkedList()
        self.c.append('not a match')
        self.c.head.next = self.n1
        self.d = SinglyLinkedList()
        self.d.head = self.n1
    
    def test_intersection(self):
        self.assertIsNone(intersection(self.a, self.b))  # no intersection
        self.assertEqual(intersection(self.c, self.d), self.n1)  # intersection

    def test_intersection_fast(self):
        self.assertIsNone(intersection_fast(self.a, self.b))  # no intersection
        self.assertEqual(intersection_fast(self.c, self.d), self.n1)  # intersection
