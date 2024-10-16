from singly_linked_list import SinglyLinkedList
from node import Node


class Queue:
    """
    Manual Implementation of a Queue ADT using a singly linked list

    :ivar sll: Singly linked list used to implement this class's method and
    create an abstraction between this class's function and its
    implementation.
    :type sll: SinglyLinkedList
    """

    def __init__(self) -> None:
        """
        Initializes an empty SinglyLinked class.
        """
        self.sll = SinglyLinkedList()

    def enqueue(self, item: int) -> None:
        """
        Add node to the end of queue(tail).

        :param item: Provided integer value that is placed at the back of
        the queue(enqueue)
        :type item: int
        :rtype: None
        """

        # create node for item
        new_node = Node(item)
        # insert node at tail
        self.sll.append(new_node)

    def dequeue(self) -> None:
        """
        Removes first node from queue(head)

        :rtype: None
        """
        self.sll.remove_head()

    def peek(self) -> Node:
        """
        Return but do not remove Node at the front of the queue

        :rtype: Node
        :raises: # TODO: Add appropriate Exception.
        """

        if self.is_empty():
            # TODO: Add appropriate Exception.
            print("Queue is empty")
        else:
            return self.sll.head.data

    def is_empty(self) -> bool:
        """
        Return True if queue is empty. If not empty, return False.

        :rtype: bool
        """
        return self.sll.is_empty()

    def size(self) -> int:
        """
        Return the number of items in the queue.

        :rtype: int
        """
        return self.sll.length()
