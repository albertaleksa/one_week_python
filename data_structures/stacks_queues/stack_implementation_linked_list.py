class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top:
            return self.top.value
        return None

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if not self.top:
            print("Stack is empty")
            return None
        if self.top == self.bottom:
            self.bottom = None
        pop_node = self.top
        self.top = self.top.next
        self.length -= 1
        return pop_node

    def is_empty(self):
        if self.length == 0:
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
print(node.value)
node = my_stack.pop()
print(node.value)
node = my_stack.pop()
print(node.value)
node = my_stack.pop()
