from linked_lists.LinkedList import LinkedList
from linked_lists.Node import Node
from linked_lists.Queue import Queue
from .Stack import MyStack

class MyQueue(LinkedList):

    _data = []

    def __init__(self, data=None):
        super().__init__(data)

    def enqueue(self, data):
        return super().enqueue(data)

    def dequeue(self):
        return super().remove_node(self.head)

    def __len__(self):
        return super().__len__()

    @property
    def data(self):
        return self._data
    
    #Calls the parent class property and passes self.
    @data.getter
    def data(self):
        return super().data

    @staticmethod
    def rearrange(queue):
        odds = MyQueue()
        current_node = queue.head

        for i in range(len(queue)):
            try:
                node = queue.remove_node(current_node)
                if (node.data % 2) == 1:
                    odds.enqueue(current_node.data)
                else:
                    queue.enqueue(node.data)
            except:
                pass

            current_node = current_node.next

        current_node = odds.head
        while current_node:
            queue.enqueue(current_node.data)

            current_node = current_node.next      

        return queue

    @staticmethod
    def isPalindrome(queue):
        length = len(queue) // 2
        stack = MyStack()
        stack.remove_node(stack.get_head_node())

        index = 0
        while index < length:
            stack.push(queue.dequeue().data)
            index += 1

        return True if queue.data == stack.data else False

