"""
Problem 2.5: You have 2 numbers represented by a linked list, where each node contains a single digit. The digits are
stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list. You are not allowed to convert the linked list to an integer.

ex: (7-1-6) + (5-9-2)  =  617 + 295
output: (2-1-9)  =  912

Follow up: repeat the above problem supposing the digits are stored in forward order.
"""
from cracking_the_coding_interview.chapter2.linkedlist.linkedlist import SinglyLinkedList
from cracking_the_coding_interview.chapter2.linkedlist.node import Node


def sum_lists_reverse(*args):
    """
    Sums singly linked lists. Each node is a digit stored in reverse order.

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
        if all(map(lambda x: x is None, nodes)) and carryover == 0:
            break

    return sum_list


def sum_lists_forward(*args):
    """
    Sums singly linked lists. Each node is a digit stored in forward order.

    :param args: SinglyLinkedLists to be summed.
    :return SinglyLinkedList: sum of inputs
    """
    #TODO: move some of this logic to other functions. Too wordy / complex.
    sum_list = SinglyLinkedList()

    # pad lists
    lengths = list(map(len, args))
    max_length = max(lengths)
    for i, arg in enumerate(args):
        pad_linked_list(arg, max_length - lengths[i])

    # sum lists
    nodes = list(map(lambda x: x.head, args))
    while True:
        # Sum data from each list
        summation = 0
        for i, node in enumerate(nodes):
            summation += node.data
            nodes[i] = node.next
        sum_list.append(summation)

        # Check if the end of a list is reached (all lists are the same length)
        if node.next is None:
            break

    # account for carryover
    while True:
        exit_flag = True
        runner = sum_list.head
        while runner.next is not None:
            carry, keep = divmod(runner.next.data, 10)
            runner.data += carry
            runner.next.data = keep
            runner = runner.next
            if carry > 0:
                exit_flag = False

        # check that head value isn't >=10
        carry, keep = divmod(sum_list.head.data, 10)
        if carry > 0:
            sum_list.head.data = keep
            pad_linked_list(sum_list, 1, value=carry)
            exit_flag = False

        if exit_flag:
            break

    return sum_list


def pad_linked_list(sll, padding, value=0):
    """
    Pad a singly linked list

    :type sll: SinglyLinkedList
    :param int padding: number of padding nodes to add
    :param value: value of padding (default = 0)
    :return: None
    """
    for i in range(padding):
        new_head = Node(value)
        new_head.next = sll.head
        sll.head = new_head
