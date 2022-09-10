class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        if len(self.array) > 0:
            return self.array[-1]
        return None

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if len(self.array) > 0:
            return self.array.pop()
        return None

    def is_empty(self):
        if len(self.array) == 0:
            return True
        return False


my_stack = Stack()
my_stack.push("google")
print(my_stack.peek())
my_stack.push("udemy")
print(my_stack.peek())
my_stack.push("youtube")
print(my_stack.peek())

node = my_stack.pop()
print(node)
node = my_stack.pop()
print(node)
node = my_stack.pop()
print(node)
node = my_stack.pop()
