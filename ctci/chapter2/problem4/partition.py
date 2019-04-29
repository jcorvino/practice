"""
Problem 2.4: Write code to partition a linked list around a value x such that all nodes less than x come before all
nodes greater than or equal to x.
Example: 3 -> 5 -> 8 -> 10  (Partition = 5)
Result: 3     ->    5 -> 8 -> 10 (Left side and right side of the partition have no particular order required)
"""


def partition(sll, p):
    """
    Partition a singly linked list. Time complexity = O(N). Space complexity = O(1).

    :type sll: SinglyLinkedList
    :param p: partition value
    :return: None
    """
    runner = sll.head
    left_node = None  # last node of left partition (<p)
    right_node = None  # last node of right partition (>=p)
    right_partition_start = None  # first node in right partition

    while runner is not None:
        if runner.data < p:
            # left partition
            if left_node is None:
                sll.head = runner
            else:
                left_node.next = runner
            left_node = runner
        else:
            # right partition
            if right_node is None:
                right_partition_start = runner
            else:
                right_node.next = runner
            right_node = runner
        runner = runner.next

    # Ensure end node.next is set to None
    if right_node is not None:
        right_node.next = None
    elif left_node is not None:
        left_node.next = None

    # link both partitions
    if left_node is not None:
        left_node.next = right_partition_start
    else:
        sll.head = right_partition_start
