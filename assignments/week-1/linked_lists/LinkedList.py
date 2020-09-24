from .Node import *


class LinkedList(Node):

    _data = []

    def __init__(self):
        self.head = None
        self._data = []

    @property
    def data(self):
        return self._data
    
    @data.getter
    def data(self):
        current_node = self.head
        while current_node:
            self._data += [current_node.data]
            current_node = current_node.next
        return self._data    

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def get_head_node(self):
        return self.head

    def enqueue(self, data):
        tail_node = self.get_tail_node()
        tail_node.next = Node(data)
        return

    def get_tail_node(self):
        current_node = self.head
        while current_node:
            if current_node.next:
                current_node = current_node.next
            else:
                return current_node

    def remove_node(self, node):
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node == node:
                try:
                    previous_node.next = current_node.next
                    return Node
                except(AttributeError):
                    node = current_node
                    self.head = current_node.next
                    return node
            else:
                previous_node = current_node
                current_node = current_node.next
                continue
        return

    def remove_data(self, data):
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == data:
                try:
                    previous_node.next = current_node.next
                    return current_node
                except(AttributeError):
                    self.head = current_node.next
                    return current_node
            else:
                previous_node = current_node
                current_node = current_node.next
                continue
        return

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next

        return length
    
    def __getitem__(self, key):
        index = 0
        current_node = self.head
        while index != key:
            current_node = current_node.next
            index += 1
        
        return current_node

    def __str__(self):
        string_list = ""
        current_node = LinkedList.get_head_node(self)
        while current_node:
            string_list += str(current_node.data) + "\n"
            current_node = current_node.next
        return string_list
