class SinglyLinkedList:
    """Implementation of a singly linked list class from scratch"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_after(self, curr_node, new_node):

        # if list is empty
        if self.head is None:
            self.append(new_node)
            return

        # if not empty, traverse the linked list to find the curr node
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
            self.size += 1

    # def remove_after(self, curr_node):
    #     """Function that handles various cases relating to removing a node after the specified one."""
    #
    #     # if list is empty: return error
    #     if self.length() == 0:
    #         print("Cannot remove node because list is empty.")
    #         return
    #
    #
    #     # special case: if None is passed: remove head
    #     if curr_node is None:
    #
    #         # if curr_node is the tail: remove head, set head & tail to None
    #         if self.head is self.tail:
    #             self.head = None
    #             self.tail = None
    #         else:
    #             # set current node's nxt ptr to the node after the node being removed
    #             self.head = self.head.next
    #
    #     # if curr_node is not None
    #     elif curr_node is not None:
    #
    #         # traverse ll, check for node existence: if node does not exist: return error
    #         current = self.head
    #         found = False
    #         while current is not None:
    #             if current == curr_node:
    #                 found = True
    #                 break
    #             current = current.next
    #
    #         if not found:
    #             print("Node does not exist in list.")
    #             return
    #
    #         # check if there is a node after curr_node
    #         if current.next is None:
    #             print("No node exists after the given current node.")
    #             return
    #
    #         # common case: removing a node somewhere in the middle of the list
    #         if curr_node is not self.tail and curr_node.next is not self.tail:
    #             curr_node.next = curr_node.next.next
    #
    #         # if curr_node's next is the tail
    #         elif curr_node.next is self.tail:
    #             self.tail = curr_node
    #             self.tail.next = None
    #             curr_node.next = None
    #
    #         # if curr_node is the tail: return error
    #         elif curr_node is self.tail:
    #             print("No node exists after tail.")
    #             return

    def remove(self):
        """Removes specified node"""

    def remove_head(self):
        """Removes head node"""
        # if list not empty:
        if self.is_empty():
            # return error
            print("List is empty.")
        else:
            if self.size == 1:
                # remove head
                self.head = self.head.next
                # adjust tail
                self.tail = self.head
                self.size -= 1
            else:
                # remove head
                self.head = self.head.next
                self.size -= 1

    def is_empty(self):
        """Checks if list is empty"""
        if self.size > 0:
            return False
        else:
            return True

    def length(self):
        """Returns an int representation of linked list's length"""
        # if list empty: return 0
        if not self.is_empty():
            # traverse list, incrementing after each visit of a node
            length = 1
            current = self.head
            while current is not self.tail:
                current = current.next
                length = length + 1
        else:
            return 0

        return length


#   def print(self):



