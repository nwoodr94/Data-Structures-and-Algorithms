from .Node import *

class LinkedList(Node):

    def __init__(self):
        self.head = None

    def push(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node
        return new_node 

    def get_head_node(self):
        return self.head

    def get_tail_node(self):
        current_node = self.head
        while current_node:
            if current_node.next:
                current_node = current_node.next
            else:
                return current_node

    def remove_node(self, Node):
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node == Node:
                try:
                    previous_node.next = current_node.next
                    return Node
                except(AttributeError):
                    node = current_node
                    self.head_node = current_node.next
                    return node
            else:
                previous_node = current_node
                current_node = current_node.next
                continue
        return

    def __str__(self):
        string_list = ""
        current_node = LinkedList.get_head_node(self)
        while current_node:
            string_list += str(current_node.data) + "\n"
            current_node = current_node.next
        return string_list