"""
Test cases for loop_detection module
"""
import unittest
from ctci.chapter2.problem8.loop_detection import loop_detection, loop_detection_fast
from ctci.chapter2.linkedlist.linkedlist import SinglyLinkedList
from ctci.chapter2.linkedlist.node import Node


class TestLoopDetection(unittest.TestCase):

    def setUp(self):
        # No loop
        self.a = SinglyLinkedList()
        self.a.append(1)
        self.a.append(2)
        self.a.append(3)

        # Empty list (no loop)
        self.b = SinglyLinkedList()

        # Loop
        self.c = SinglyLinkedList()
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n1.next = self.n2
        self.n2.next = self.n3
        self.n3.next = self.n1
        self.c.append('not part of loop')
        self.c.append('also not part of loop')
        self.c.head.next.next = self.n1

    def test_loop_detection(self):
        # No loop
        self.assertIsNone(loop_detection(self.a))

        # Empty list (no loop)
        self.assertIsNone(loop_detection(self.b))

        # Loop
        self.assertIs(loop_detection(self.c), self.n1)

    def test_loop_detection_fast(self):
        # No loop
        self.assertIsNone(loop_detection_fast(self.a))

        # Empty list (no loop)
        self.assertIsNone(loop_detection_fast(self.b))

        # Loop
        self.assertIs(loop_detection_fast(self.c), self.n1)
