class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if len(self.array) > 0:
            return self.array.pop()
        return None

    def peek(self):
        if len(self.array) > 0:
            return self.array[-1]
        return None

    def is_empty(self):
        if len(self.array) == 0:
            return True
        return False


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.front = None

    def push(self, element):
        if not element:
            print("invalid value")
        else:
            if self.stack1.is_empty():
                self.front = element
            self.stack1.push(element)

    def _fill_first_stack(self, s1, s2):
        while not s2.is_empty():
            item = s2.pop()
            s1.push(item)

    def pop(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            self.front = None
        if not self.stack2.is_empty():
            self.front = self.stack2.peek()
        return self.front

    def empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()


my_queue = MyQueue()
my_queue.push(1) # queue is: [1]
print(f"stack1 = {my_queue.stack1.array} stack2 = {my_queue.stack2.array} front = {my_queue.front}")
print(my_queue.peek()) # return 1
print(my_queue.pop()) # return 1, queue is [2]
print(f"stack1 = {my_queue.stack1.array} stack2 = {my_queue.stack2.array} front = {my_queue.front}")
print(my_queue.peek())
print(my_queue.empty()) # return false


