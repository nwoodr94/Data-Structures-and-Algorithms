from linked_lists.Queue import Queue

queue = Queue(0)

def test_isInstance():
    assert isinstance(queue, Queue)

def test_enqeue():
    queue.enqueue(1)
    assert len(queue) == 2