from assignment.Stack import MyStack

stack = MyStack(0)

def test_isinstance():
    assert isinstance(stack, MyStack)

def test_copyStack():
    stack.push(1)
    stack.push(2)
    stack.push(3)
    copy = MyStack.copyStack(stack)
    assert copy.data == stack.data