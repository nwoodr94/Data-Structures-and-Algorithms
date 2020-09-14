from .LinkedList import *

class Queue(LinkedList):

    def __init__(self, data):
        self.head_node = Node(data)

    def enqueue(self, data):
        super().insert_tail_node(data)

    def dequeue(self):
        node = super().get_head_node()
        super().remove_node(node)
        return node