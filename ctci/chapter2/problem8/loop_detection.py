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


# Second attempt at loop_detection function using a faster method.
def loop_detection_fast(sll):
    """
    Returns the node at the start of a loop. If no loop is detected return None.
    Time complexity = O(N). Space complexity = O(1).

    :type sll: SinglyLinkedList
    :return Node: start of loop
    """
    collision_node = get_collision_node(sll)
    if collision_node is None:
        return None

    # Collision will occur K points before the start of the loop.
    # K is the length of the non-loop portion of the list.
    # Now two runners can be started (one at head, one at collision node). They will collide at the loop start.
    head_runner = sll.head
    loop_runner = collision_node
    while True:
        if head_runner is loop_runner:
            return head_runner
        head_runner = head_runner.next
        loop_runner = loop_runner.next


def get_collision_node(sll):
    """
    Uses a fast runner (increments by 2) and a slow runner (increments by 1) to determine if a loop occurs.
    Returns the collision point of a singly linked list with a loop. Returns None if no collision occurs.

    :type sll: SinglyLinkedList
    :return Node: collision point
    """
    slow_runner = sll.head  # increments by 1
    fast_runner = sll.head  # increments by 2

    while True:
        try:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
        except AttributeError:  # fast_runner is none
            return None
        else:
            if slow_runner is fast_runner:  # collision node
                return slow_runner
