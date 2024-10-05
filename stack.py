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
        self.sll.prepend(node)

    def pop(self):
        """Returns and removes item from top of stack (head of list)"""
        # if stack not empty
        if self.sll.not_empty():
            popped_item = self.sll.head.data
            self.sll.remove_head()
            return popped_item
        else:
            print("Cannot pop item because stack is empty")
            return

    def peek(self):
        """Returns top of stack, but does not remove it."""
        # check if list is empty
        if self.sll.not_empty():
            # return head
            return self.sll.head.data
        else:
            print("Cannot pop item because stack is empty")
            return

    def is_empty(self):
        if self.sll.not_empty():
            return False
        else:
            return True

    def get_length(self):
         # return len of underlying ll
        return self.sll.length()


