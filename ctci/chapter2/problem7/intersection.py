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
    # Get end node and length of both lists
    end_node_a, length_a = get_end_node(a)
    end_node_b, length_b = get_end_node(b)
    diff = abs(length_a - length_b)

    # If the end nodes are not the same, the lists do not intersect
    # (return end nodes so intersection function has less to check)
    if end_node_a is not end_node_b:
        return end_node_a, end_node_b

    # Define simple function to move node forward "dist" number of places
    def move(node, dist):
        for _ in range(dist):
            node = node.next
        return node

    # Make lists the same length so the intersection node will match up
    if diff > 0:
        if length_a > length_b:  # move a
            return move(a.head, diff), b.head
        else:  # move b
            return a.head, move(b.head, diff)
    else:  # same len
        return a.head, b.head


def get_end_node(sll):
    """
    Get the length and end node of a singly linked list

    :type sll: SinglyLinkedList
    :return Node, int: end node, length
    """
    if sll.head is None:  # empty list
        return None, 0

    # Get list length and end node
    node = sll.head
    length = 1
    while node.next is not None:
        length += 1
        node = node.next
    return node, length
