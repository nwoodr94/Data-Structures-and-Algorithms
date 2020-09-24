from linked_lists.LinkedList import LinkedList
from linked_lists.Node import Node
from linked_lists.Queue import Queue

class MyStack(LinkedList):

    def __init__(self, data):
        self.head = Node(data)

    def push(self, data):
        return super().push(data)

    def pop(self):
        return super().remove_node(self.head)

    @staticmethod
    def copyStack(stack):
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