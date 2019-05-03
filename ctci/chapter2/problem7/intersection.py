"""
Problem 2.7: Given two singly linked lists, determine if the two lists intersect. Return the intersecting node.
"""


def intersection(a, b):
    """
    Determines if two singly linked lists intersect and if so returns the intersecting node. Else returns None.
    Time complexity = O(N * M) where N is len(a) and M is len(b). Space complexity = O(1).

    :type a: SinglyLinkedList
    :type b: SinglyLinkedList
    :return Node: intersection node
    """
    node_a = a.head
    node_b = b.head
    while node_a is not None:
        while node_b is not None:
            if node_a is node_b:
                return node_a
            node_b = node_b.next
        node_b = b.head
        node_a = node_a.next
    return None


# Second attempt at intersection function using a faster method.
def intersection_fast(a, b):
    """
    Determines if two singly linked lists intersect and if so returns the intersecting node. Else returns None.
    Time complexity = O(N + M) where N is len(a) and M is len(b). Space complexity = O(1).

    :type a: SinglyLinkedList
    :type b: SinglyLinkedList
    :return Node: intersection node
    """
    node_a, node_b = make_same_len(a, b)  # now both lists have the same length

    while node_a is not None:
        if node_a is node_b:
            return node_a
        else:
            node_a = node_a.next
            node_b = node_b.next
    return None


def make_same_len(a, b):
    """
    Takes two linked lists and moves the beginning of the longer list so that both lists are now the same length.
    Returns the starting nodes, but does NOT modify the linked list objects. Time complexity = O(N + M) where N is
    len(a) and M is len(b). Space complexity = O(1).

    :type a: SinglyLinkedList
    :type b: SinglyLinkedList
    :return Node, Node: starting nodes
    """
    length_a = len(a)
    length_b = len(b)
    diff = abs(length_a - length_b)

    def move(node, dist):
        for _ in range(dist):
            node = node.next
        return node

    if diff > 0:
        if length_a > length_b:  # move a
            return move(a.head, diff), b.head
        else:  # move b
            return a.head, move(b.head, diff)
    else:  # same len
        return a.head, b.head

