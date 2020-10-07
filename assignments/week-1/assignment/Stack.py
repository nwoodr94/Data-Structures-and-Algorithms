from linked_lists.LinkedList import LinkedList
from linked_lists.Node import Node
from linked_lists.Queue import Queue

class MyStack(LinkedList):

    _data = []

    def __init__(self, data=None):
        self.head = Node(data)

    @property
    def data(self):
        return self._data
    
    #Calls the parent class property and passes self.
    @data.getter
    def data(self):
        return super().data

    def push(self, data):
        return super().push(data)

    def pop(self):
        return super().remove_node(self.head)

    @staticmethod
    def copyStack(stack):
        """
        Accepts a stack and returns a deep copy by loading nodes into an intermediary queue.

        """
        current_node = stack.head
        queue = Queue(current_node)
        while current_node:
            queue.enqueue(current_node)
            current_node = current_node.next

        current_node = queue.head
        copy = MyStack(queue.head)
        while current_node:
            copy.push(current_node)
            current_node = current_node.next
        
        return copy

    def __len__(self):
        return super().__len__()