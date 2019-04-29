from .node import Node


class SinglyLinkedList:
    """
    A singly linked list
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        out = []
        n = self.head
        while n is not None:
            out.append(str(n))
            n = n.next

        return 'SinglyLinkedList(' + ','.join(out) + ')'

    def __eq__(self, other):
        """
        Simple implementation of __eq__ to check if all elements of both SinglyLinkedLists contain the same data.
        """
        if not isinstance(other, SinglyLinkedList):
            return False

        node = self.head
        other_node = other.head
        while True:
            if node.next is None or other_node.next is None:
                if node.next is other_node.next:
                    return True
                else:
                    return False
            elif node.data != other_node.data:
                return False
            node = node.next
            other_node = other_node.next

    def __len__(self):
        """
        Simple implementation of __len__. Time complexity = O(N).
        """
        counter = 0
        node = self.head
        while node is not None:
            counter += 1
            node = node.next
        return counter

    def append(self, data):
        """
        Appends data to tail of SinglyLinkedList
        """
        end_node = Node(data)
        if self.head is None:
            self.head = end_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = end_node

    def remove(self, node):
        """
        Deletes a node. Will do nothing if node is not in SinglyLinkedList
        """
        if self.head is node:
            self.head = node.next
        else:
            n = self.head
            while n is not None:
                if n.next is node:
                    n.next = node.next
                    break
                n = n.next


class DoublyLinkedList:
    """
    A doubly linked list
    """
    pass
