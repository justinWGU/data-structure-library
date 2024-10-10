import pytest
from data_structures.stack import Stack


def test_stack_is_empty():
    stack = Stack()
    assert stack.size() == 0
    assert stack.is_empty() == True


def test_stack_push():
    stack = Stack()
    stack.push(3)
    assert stack.size() == 1


def test_stack_peek():
    stack = Stack()
    stack.push(3)
    assert stack.peek() == 3
    assert stack.size() == 1


def test_stack_pop():
    stack = Stack()
    stack.push(3)
    assert stack.pop() == 3
    assert stack.size() == 0
