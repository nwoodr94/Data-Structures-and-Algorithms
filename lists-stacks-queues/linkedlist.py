from node import Node

class LinkedList(Node):

    def __init__(self, data):
        self.head_node = Node(data)

    def insert_head_node(self, data=None):
        new_node = Node(data)
        new_node.set_next(self.head_node)
        self.head_node = new_node
        return new_node

    def get_head_node(self):
        return self.head_node

    def insert_tail_node(self, data=None):
        new_node = Node(data)
        self.get_tail_node().set_next(new_node)
        return new_node

    def get_tail_node(self):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_next():
                current_node = current_node.get_next()
            else:
                return current_node

    def remove_node(self, Node):
        previous_node = None
        current_node = self.get_head_node()
        while current_node:
            if current_node == Node:
                try:
                    previous_node.set_next(current_node.get_next())
                    return Node
                except(AttributeError):
                    node = current_node
                    self.head_node = current_node.get_next()
                    return node
            else:
                previous_node = current_node
                current_node = current_node.get_next()
                continue
        return

    def __str__(self):
        string_list = ""
        current_node = LinkedList.get_head_node(self)
        while current_node:
            string_list += str(current_node.get_data()) + "\n"
            current_node = current_node.get_next()
        return string_list