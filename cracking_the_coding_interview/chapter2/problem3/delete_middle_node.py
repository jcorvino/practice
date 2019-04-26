"""
Problem 2.3: Implement ann algorithm to delete a node in the middle of a singly linked list (not head or end node).
"""


def delete_middle_node(sll, node):
    """
    Remove a middle node (not head or end node) from a singly linked list.
    Time complexity = O(N). Space complexity = O(1).

    :type sll: SinglyLinkedList
    :type node: Node
    :return: None
    """
    curr = sll.head  # current node

    while curr.next is not None:
        if curr.next is node:
            curr.next = node.next
            break
        curr = curr.next

