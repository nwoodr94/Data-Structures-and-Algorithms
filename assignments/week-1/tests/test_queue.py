from assignment.Queue import MyQueue

queue = MyQueue(0)

def test_isInstance():
    assert isinstance(queue, MyQueue)

def test_queueLen():
    assert len(queue)

def test_enqeue():
    queue.enqueue(1)
    assert len(queue) == 2

def test_dequeue():
    queue.dequeue()
    assert len(queue) == 1