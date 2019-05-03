"""
Test cases for loop_detection module
"""
import unittest
from ctci.chapter2.problem8.loop_detection import loop_detection
from ctci.chapter2.linkedlist.linkedlist import SinglyLinkedList
from ctci.chapter2.linkedlist.node import Node


class TestLoopDetection(unittest.TestCase):

    def test_loop_detection(self):
        # No loop
        a = SinglyLinkedList()
        a.append(1)
        a.append(2)
        a.append(3)
        self.assertIsNone(loop_detection(a))

        # Empty list (no loop)
        b = SinglyLinkedList()
        self.assertIsNone(loop_detection(b))

        # Loop
        c = SinglyLinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n1.next = n2
        n2.next = n3
        n3.next = n1
        c.append('not part of loop')
        c.append('also not part of loop')
        c.head.next.next = n1
        self.assertIs(loop_detection(c), n1)
