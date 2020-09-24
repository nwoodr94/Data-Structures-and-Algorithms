from .LinkedList import *
from .Queue import *


class Stack(LinkedList):

    def __init__(self, data):
        self.head = Node(data)

    def push(self, data):
        super().push(data)

    def pop(self):
        super.remove_node(self.head)
