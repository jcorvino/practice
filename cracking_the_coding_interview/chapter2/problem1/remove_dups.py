"""
Problem 2.1: Write code to remove duplicates from an unsorted linked list.
"""


def remove_dups(linkedlist):
    """
    Remove duplicates from a linked list.
    Time complexity = O(N**2)

    :param linkedlist: A SinglyLinkedList
    :return None: Modifies list in place.
    """
    unique_data = []

    n = linkedlist.head
    while n is not None:
        if n.data in unique_data:
            prev.next = n.next
            n = prev  # move n back 1 link so the duplicate is ignored
        else:
            unique_data.append(n.data)
        prev = n
        n = n.next


