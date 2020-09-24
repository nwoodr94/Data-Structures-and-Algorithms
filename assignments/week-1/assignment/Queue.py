from linked_lists.LinkedList import LinkedList
from linked_lists.Node import Node

class MyQueue(LinkedList):

    def __init__(self, data):
        self.head = Node(data)

    def enqueue(self, data):
        return super().enqueue(data)

    def dequeue(self):
        return super().remove_node(self.head)

    def __len__(self):
        return super().__len__()