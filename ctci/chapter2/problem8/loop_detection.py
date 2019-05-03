"""
Problem 2.8: Given a linked list which might contain a loop, implement an algorithm that returns the node at the
beginning of the loop (if on exists).
"""


def loop_detection(sll):
    """
    Returns the node at the start of a loop. If no loop is detected then return None. All nodes in the linked list must
    be hashable. Time complexity = O(N). Space complexity = O(N).

    :type sll: SinglyLinkedList
    :return Node: start of loop
    """
    node = sll.head
    unique_nodes = {}

    while node is not None:
        try:
            unique_nodes[node]
        except KeyError:
            unique_nodes[node] = None
        else:
            return node  # if node is a repeat
        node = node.next

    return None  # if no loop found
