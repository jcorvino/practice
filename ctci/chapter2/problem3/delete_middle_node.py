"""
Problem 2.3: Implement ann algorithm to delete a node in the middle of a singly linked list (not head or end node).
"""


def delete_middle_node(node):
    """
    Remove a middle node (not head or end node) from a singly linked list.
    Time complexity = O(1). Space complexity = O(1).

    :type node: Node
    :return: None
    """
    node.data = node.next.data
    node.next = node.next.next

