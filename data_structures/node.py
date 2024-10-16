class Node:
    """
        Represents a Node class for building a singly linked list.

        :ivar data: Holds the node's integer value.
        :type data: int
        :ivar next: Reference to the following node in the list.
        :type next: Optional[Node]
    """

    def __init__(self, data: int) -> None:
        """
        Initialize the node with the provided data.

        :param data: The integer value that the node will store.
        :type data: int
        :rtype: None
        """
        self.data = data
        self.next = None
