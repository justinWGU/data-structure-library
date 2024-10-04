class Node:
    """Node class to build a singly linked list"""

    def __init__(self, data): # Node initialized w/ data, but not with Node
        self.data = data
        self.next = None