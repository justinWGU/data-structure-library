from singly_linked_list import SinglyLinkedList
from node import Node


class Queue:
    """Manual Implementation of a Queue ADT using a singly linked list"""

    def __init__(self):
        self.sll = SinglyLinkedList()

    def enqueue(self, item):

        """Adds node to end of queue (tail)"""
        # create node for item
        new_node = Node(item)
        # insert node at tail
        self.sll.append(new_node)

    def dequeue(self):
        """Removes first node from queue (head)"""
        self.sll.remove_head()

    def peek(self):
        """Returns but does not remove item at the front of the queue"""
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.sll.head.data

    def is_empty(self):
        """Returns true if queue has no items"""
        return self.sll.is_empty()

    def size(self):
        """Returns the number of items in the queue"""
        return self.sll.length()
