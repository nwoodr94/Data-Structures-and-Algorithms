# Workspace
from assignment.Queue import *
from assignment.Stack import *

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
print(rearrangedQueue.data)