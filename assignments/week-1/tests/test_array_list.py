from assignment.ArrayList import ArrayList

def test_remove_front():
    arrlist = ArrayList([8, 17, 9, 24, 42, 3, 8])
    arrlist.removeFront(4)
    assert arrlist.data == [42, 3, 8]

def test_remove_back():    
    arrlist = ArrayList([8, 17, 9, 24, 42, 3, 8])
    arrlist.removeBack(4)
    assert arrlist.data == [8, 17, 9]

def test_remove_all():
    arrlist = ArrayList(["a", "b", "c", "d", "a", "d", "d", "e", "f", "d"])
    arrlist.removeAll("d")
    assert arrlist.data == ['a', 'b', 'c', 'a', 'e', 'f']

def test_stretch():
    arrlist = ArrayList([18.2, 7.5, 4.2, 24.9])
    arrlist.stretch(3)
    assert arrlist.data == [4.2, 4.2, 4.2, 7.5, 7.5, 7.5, 18.2, 18.2, 18.2, 24.9, 24.9, 24.9]