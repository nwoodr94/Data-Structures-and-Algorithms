from linked_lists.LinkedList import LinkedList
from linked_lists.Node import Node
from linked_lists.Queue import Queue

class MyQueue(LinkedList):

    def __init__(self, data=None):
        self.head = Node(data)

    def enqueue(self, data):
        return super().enqueue(data)

    def dequeue(self):
        return super().remove_node(self.head)

    def __len__(self):
        return super().__len__()

    @property
    def data(self):
        return super().data
    
    #Calls the parent class property by passing self.
    @data.getter
    def data(self):
        return LinkedList.data.fget(self)

    @staticmethod
    def rearrange(queue):
        odds = Queue()
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

        current_node = odds.head.next
        while current_node:
            queue.enqueue(current_node.data)

            current_node = current_node.next      

        return queue
