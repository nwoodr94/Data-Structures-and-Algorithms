from linked_lists import LinkedList, Node

class MyLinkedList(LinkedList):

    def __init__(self):
        self.head = None

    def insert_head_node(self, data=None):
        return super().push(data=data)

    def insert_tail_node(self, data=None):
        return super().insert_tail_node(data=data)

    def get_head_node(self):
        return super().get_head_node()

    def get_tail_node(self):
        return super().get_tail_node()

    def remove_data(self, data):
        return super().remove_data(data)

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

    @staticmethod
    def transfer(src_linked_lst, dest_linked_lst, data):
        current_node = src_linked_lst.get_head_node()
        while current_node:
            if current_node.data in data:
                transfer = src_linked_lst.remove_data(current_node.data)
                dest_linked_lst.insert_head_node(transfer)
                current_node = current_node.next
            else:
                current_node = current_node.next