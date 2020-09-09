from linkedlist import *

class Stack(LinkedList):

    def __init__(self, data):
        self.head_node = Node(data)

    def push(self, data):
        super().insert_head_node(data)

    def pop(self):
        node = super().remove_node(self.head_node)
        self.remove_node(node)
        return node