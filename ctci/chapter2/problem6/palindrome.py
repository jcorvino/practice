"""
Problem 2.6: Implement a function to check if a list is a palindrome.
"""
from math import ceil
from ctci.chapter2.problem2.k_to_last import k_to_last


def palindrome(sll):
    """
    Determines if a singly linked list is a palindrome. Time complexity = O(N**2). Space complexity = O(1).

    :type sll: SinglyLinkedList
    :return bool: True if palindrome, false otherwise
    """

    node = sll.head
    counter = 1
    half_len = ceil(len(sll) / 2)

    while node is not None:
        if counter >= half_len:
            break
        elif node.data != k_to_last(sll, counter):
            return False
        else:
            counter += 1
            node = node.next
    return True
