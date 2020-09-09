class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_next(self, Node):
        self.next = Node
    
    def get_next(self):
        return self.next

    def set_prev(self, Node):
        self.prev = Node

    def get_prev(self):
        return self.prev

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data