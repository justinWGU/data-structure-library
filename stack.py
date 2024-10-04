from singly_linked_list import SinglyLinkedList
from node import Node

class Stack:
    def __init__(self):
        self.sls = SinglyLinkedList()

    def push(self, item):
        # create a node for item
        node = Node(item)
        # append node to list
        self.sls.append(node)

