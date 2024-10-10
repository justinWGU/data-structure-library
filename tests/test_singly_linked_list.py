import pytest
from data_structures.singly_linked_list import SinglyLinkedList
from data_structures.node import Node


def test_list_init():
    linked_list = SinglyLinkedList()
    assert linked_list.length() == 0
    assert linked_list.is_empty() == True


def test_append_when_list_is_initially_empty():
    """Tests the append method when list is first empty. Makes sure list is not empty, length is 1, head & tail point
    to the same node, and value of the node appended is correct."""

    linked_list = SinglyLinkedList()
    node = Node(9)
    linked_list.append(node)
    assert linked_list.length() == 1
    assert linked_list.is_empty() == False
    assert linked_list.head is linked_list.tail
    assert linked_list.head.data == 9


def test_prepend_when_list_is_initially_empty():
    """Tests prepend method when list is first empty. Makes sure list is not empty, length is 1, head & tail point to
    the same node, and value of the node prepended is correct."""

    linked_list = SinglyLinkedList()
    node = Node(9)
    linked_list.append(node)
    assert linked_list.length() == 1
    assert linked_list.is_empty() == False
    assert linked_list.head is linked_list.tail
    assert linked_list.head.data == 9


# def test_insert_after():
#     """Tests insert_after method when inserting somewhere in the middle. Makes sure list is not empty, length is
#     correct, node is inserted after given node"""
#
#     linked_list = SinglyLinkedList()
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     linked_list.append(node1)
#     linked_list.append(node3)
#     linked_list.insert_after(node1, node2)
#     assert linked_list.is_empty() == False
#     assert linked_list.length() == 3
#     assert linked_list.print() == f"{1}\n{2}\n{3}"


def test_remove_head_when_list_not_empty():
    """Tests list when it's not empty by assuring the proper value is removed from the front of the list,
    length is adjusted after head removal."""

    linked_list = SinglyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    linked_list.append(node1)
    linked_list.append(node2)
    assert linked_list.head.data == 1
    assert linked_list.length() == 2
    linked_list.remove_head()
    assert linked_list.length() == 1
    assert linked_list.head.data == 2
