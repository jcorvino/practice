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
        while n.next is not None:
            out.append(str(n))
            n = n.next
        out.append(str(n))  # end node

        return 'SinglyLinkedList(' + ','.join(out) + ')'

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
