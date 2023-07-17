from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    new_priority_queue = PriorityQueue()
    new_priority_queue.enqueue({"qtd_linhas": 2})

    assert len(new_priority_queue) == 1

    new_priority_queue.enqueue({"qtd_linhas": 6})
    assert len(new_priority_queue) == 2

    assert new_priority_queue.dequeue() == {"qtd_linhas": 2}

    new_priority_queue.enqueue({"qtd_linhas": 1})
    assert new_priority_queue.search(0) == {"qtd_linhas": 1}

    with pytest.raises(IndexError):
        new_priority_queue.search(404)
