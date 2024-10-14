class Node:
    """
    Represents a Node class for building a singly linked list.

    Attributes:
        data: Holds the node's integer value.
        next: Reference to the following node in the list.
    """

    def __init__(self, data):

        """
        Initialize the node with the provided data.

        Args:
            data: The integer value that the node will store.
        """
        self.data = data
        self.next = None
