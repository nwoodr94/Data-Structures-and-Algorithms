from linked_lists import LinkedList, Node

class MyLinkedList(LinkedList):

    def __init__(self):
        self.head = None

    def insert_head_node(self, data=None):
        return super().push(data=data)

    def insert_tail_node(self, data=None):
        return super().insert_tail_node(data=data)

    def get_next(self):
        return self.head_node.get_next()

    def set_next(self, Node):
        return super().set_next(Node)

    def get_head_node(self):
        return super().get_head_node()

    def get_tail_node(self):
        return super().get_tail_node()

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 