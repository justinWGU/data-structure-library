import pytest
from data_structures.queue import Queue


def test_que_is_empty():
    queue = Queue()
    assert queue.is_empty() == True
    assert queue.size() == 0


def test_enqueue():
    queue = Queue()
    queue.enqueue(5)
    assert queue.size() == 1


def test_dequeue():
    queue = Queue()
    queue.enqueue(5)
    queue.dequeue()
    assert queue.size() == 0


def test_peek():
    queue = Queue()
    queue.enqueue(5)
    assert queue.peek() == 5
    assert queue.size() == 1

