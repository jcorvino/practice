"""
Problem 2.1: Write code to remove duplicates from an unsorted linked list.

Follow up: What if you are not allowed to use buffers?
Answer: same approach as remove_dups, but instead of checking
"if n.data in unique_data", check if n.data equals any other linked list node. This would also take O(N**2) time, but
space complexity would be O(1) without a buffer.
"""


def remove_dups(linkedlist):
    """
    Remove duplicates from a linked list. Linked list data can be any type (accepts non-hashable data)
    Time complexity = O(N**2)

    :param linkedlist: A SinglyLinkedList
    :return None: Modifies list in place.
    """
    unique_data = []

    n = linkedlist.head
    while n is not None:
        if n.data not in unique_data:
            unique_data.append(n.data)
        else:
            prev.next = n.next
            n = prev  # move n back 1 link so the duplicate is ignored
        prev = n
        n = n.next


def remove_dups_hashable(linkedlist):
    """
    Remove duplicates from a linked list. Requires all linked list data to be hashable (e.g. no lists!)
    Time complexity = O(N)

    :param linkedlist: A SinglyLinkedList (all data in the linked list must be hashable)
    :return None: Modifies list in place.
    """
    unique_data = {}

    n = linkedlist.head
    while n is not None:
        try:
            unique_data[n.data]
        except KeyError:
            unique_data[n.data] = None
        else:
            prev.next = n.next
            n = prev  # move n back 1 link so the duplicate is ignored
        prev = n
        n = n.next


