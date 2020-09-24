from assignment.LinkedList import MyLinkedList
from linked_lists.Node import Node

llist = MyLinkedList(0)

def test_isInstance():
    assert isinstance(llist, MyLinkedList)

def test_insertData():
    llist.insert_head_node(1)
    llist.insert_tail_node(2)
    assert len(llist) == 3

def test_data():
    assert llist.data == [1, 0 ,2]

def test_removeHead():
    llist.remove_data(1)
    assert len(llist) == 2

def test_removeTail():
    llist.remove_data(2)
    assert len(llist) == 1

def test_isSubscriptable():
    assert isinstance(llist[0], Node)