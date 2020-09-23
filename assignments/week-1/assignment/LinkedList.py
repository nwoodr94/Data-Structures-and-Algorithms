from linked_lists import LinkedList, Node

class MyLinkedList(LinkedList):

    def __init__(self, data):
        self.head = Node(data)

    def insert_head_node(self, data=None):
        return super().push(data=data)

    def insert_tail_node(self, data=None):
        return super().enqueue(data=data)

    def get_head_node(self):
        return super().get_head_node()

    def get_tail_node(self):
        return super().get_tail_node()

    def remove_data(self, data):
        return super().remove_data(data)

    def __getitem__(self, key):
        index = 0
        current_node = self.head
        while index != key:
            current_node = current_node.next
            index += 1
        
        return current_node

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next

        return length

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