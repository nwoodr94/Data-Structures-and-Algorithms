from .LinkedList import *


class Queue(LinkedList):

    def __init__(self, data):
        self.head = Node(data)

    def enqueue(self, data):
        super().enqueue(data)

    def dequeue(self):
        super().remove_node(self.head)
