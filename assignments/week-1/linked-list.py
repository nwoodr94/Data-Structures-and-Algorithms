class LinkedList:

    head_node = None

    def __init__(self, link=None):
        self.head_node = Node()
        self.link = link
    
    def get_next_node(self):
        return head_node.link







class Node:

    def __init__(self, data, node=None):
        self.data = data
        self.next = node