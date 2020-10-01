from .LinkedList import *


class Queue(LinkedList):

    def __init__(self, data=None):
        self.head = Node(data)

    def enqueue(self, data):
        super().enqueue(data)

    def dequeue(self):
        super().remove_node(self.head)
