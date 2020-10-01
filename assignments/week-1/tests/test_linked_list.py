from assignment.LinkedList import MyLinkedList
from linked_lists.Node import Node

def test_isInstance():
    llist = MyLinkedList(0)
    assert isinstance(llist, MyLinkedList)

def test_insertData():
    llist = MyLinkedList(0)
    llist.insert_head_node(1)
    llist.insert_tail_node(2)
    assert len(llist) == 3

def test_data():
    llist = MyLinkedList(1)
    llist.insert_head_node(2)
    llist.insert_tail_node(3)
    assert llist.data == [2, 1 ,3]

def test_removeHead():
    llist = MyLinkedList(0)
    llist.insert_head_node(1)
    llist.remove_data(1)
    assert len(llist) == 1

def test_removeTail():
    llist = MyLinkedList(0)
    llist.insert_tail_node(2)
    llist.remove_data(2)
    assert len(llist) == 1

def test_isSubscriptable():
    llist = MyLinkedList(0)
    assert isinstance(llist[0], Node)