"""
Problem 2.2: Implement an algorithm to find the kth to last element of a singly linked list.
"""


def k_to_last(sll, k):
    """
    Find the k to last element of the SinglyLinkedList. Time complexity = O(N). Space complexity = O(1).

    :type sll: SinglyLinkedList
    :type k: int
    :return: data from the k to last node (k=1 returns end node).
    :raises ValueError: if k is greater than the list length.
    """
    if k < 1:
        raise ValueError('k must be greater than 1. k=%s' % str(k))

    # end_runner goes to the end of the list. k_runner remains k-1 elements behind end_runner
    k_runner = sll.head
    end_runner = sll.head
    counter = 1
    while end_runner.next is not None:
        end_runner = end_runner.next
        if counter < k:
            counter += 1
        else:
            k_runner = k_runner.next

    if counter < k:  # raise error if list is shorter than k
        raise ValueError('k=%s which is longer than the SinglyLinkedList (len=%s)' % (str(k), str(counter)))

    return k_runner.data
