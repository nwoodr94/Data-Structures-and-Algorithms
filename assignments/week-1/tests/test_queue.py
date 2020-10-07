from assignment.Queue import *

def test_isInstance():
    queue = MyQueue()
    assert isinstance(queue, MyQueue)

def test_queueLen():
    queue = MyQueue()
    assert len(queue) == 0

def test_enqeue():
    queue = MyQueue()
    queue.enqueue(0)
    assert len(queue) == 1

def test_dequeue():
    queue = MyQueue()
    queue.enqueue(1)
    queue.dequeue()
    assert len(queue) == 0

def test_rearrage():
    queue = MyQueue()
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(17)
    queue.enqueue(6)
    queue.enqueue(83)
    queue.enqueue(1)
    queue.enqueue(84)
    queue.enqueue(16)
    queue.enqueue(37)
    rearrangedQueue = MyQueue.rearrange(queue)
    assert rearrangedQueue.data == [4, 6, 84, 16, 3, 5, 17, 83, 1, 37] 

def test_isPalindrome():
    queue = MyQueue()
    queue.enqueue(3)
    queue.enqueue(5) 
    queue.enqueue(4) 
    queue.enqueue(17) 
    queue.enqueue(6) 
    queue.enqueue(6) 
    queue.enqueue(17)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(3)
    assert MyQueue.isPalindrome(queue) == True
     



