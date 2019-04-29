class Node:
    """
    A node in a LinkedList
    """
    def __init__(self, data):
        self.next = None
        self.prev = None  # only used in DoublyLinkedList
        self.data = data

    def __str__(self):
        return str(self.data)
