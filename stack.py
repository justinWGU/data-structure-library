from singly_linked_list import SinglyLinkedList
from node import Node

class Stack:
    """Manual Implementation of Stack ADT using a singly linked list"""

    def __init__(self):
        self.sll = SinglyLinkedList()

    def push(self, item):
        # create a node for item
        node = Node(item)
        # append node to list
        self.sll.append(node)

    def get_length(self):
         # return len of underlying ll
        return self.sll.length()
