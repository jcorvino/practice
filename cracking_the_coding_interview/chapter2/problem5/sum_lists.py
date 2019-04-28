"""
Problem 2.5: You have 2 numbers represented by a linked list, where each node contains a single digit. The digits are
stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list. You are not allowed to convert the linked list to an integer.

ex: (7-1-6) + (5-9-2)  =  617 + 295
output: (2-1-9)  =  912

Follow up: repeat the above problem supposing the digits are stored in forward order.
"""
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList


def sum_lists_reverse(*args):
    """
    Sums two singly linked lists. Each node is a digit stored in reverse order.

    :param args: SinglyLinkedLists to be summed.
    :return SinglyLinkedList: sum of inputs
    """
    sum_list = SinglyLinkedList()
    nodes = list(map(lambda x: x.head, args))  # head node of each SinglyLinkedList
    carryover = 0

    while True:
        # Sum data from each list
        summation = carryover
        for i, node in enumerate(nodes):
            if node is None:
                continue
            summation += node.data
            nodes[i] = node.next

        # Account for addition carryover
        carryover, summation = divmod(summation, 10)
        sum_list.append(summation)

        # Check for end of all lists
        if all(map(lambda x: x is None, nodes)):
            break

    return sum_list
