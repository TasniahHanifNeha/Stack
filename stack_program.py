print("")


class Stack:
    def __init__(self):
        self.my_stack = []

    def is_empty(self):
        return self.my_stack == []

    def push(self, value):
        self.my_stack.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
        return self.my_stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        print("Peek Element :", self.my_stack[-1])

    def size(self):
        print("Length of the stack :", len(self.my_stack))

    def display(self):
        print("Display :", self.my_stack)
s = Stack()
s.is_empty()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.display()
s.peek()

s.pop()
s.display()
s.peek()

s.size()





print("")
























