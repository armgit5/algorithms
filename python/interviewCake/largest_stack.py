# https://www.interviewcake.com/question/python/largest-stack?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email

arr = [1,3,6,2,7,9]

class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

class MaxStack:

    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.max_stack.peek() is None or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.max_stack.peek():
            self.max_stack.pop()
        return(item)

    def get_max(self):
        return self.max_stack.peek()

ms = MaxStack()
ms.push(3)
ms.push(5)
ms.push(4)
ms.push(2)
print(ms.get_max())
print(ms.pop())
print(ms.pop())
print(ms.pop())
print(ms.get_max())



