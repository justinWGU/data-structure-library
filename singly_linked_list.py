from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        # if head == null:
            # head & tail == new_node
        # else:
            # nn's next = head
            # head = nn
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, curr_node, new_node):

        # if list is empty
        if self.head is None:
            self.append(new_node)
            return

        # traverse the linked list to find the curr node
        current = self.head
        while current is not None and current is not curr_node:
            current = current.next

        # if node doesnt exist
        if current is None:
            print(f"Node is not found in the list")

        # elif node is already tail
        elif curr_node is self.tail:
            self.append(new_node)

        # else node exists but is not tail
        else:
            new_node.next = curr_node.next
            curr_node.next = new_node



