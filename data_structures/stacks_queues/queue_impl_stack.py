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
        if self.stack1.is_empty():
            self.stack1.push(element)
            self.front = element
        else:
            self._fill_first_stack(self.stack2, self.stack1)
            self.stack1.push(element)
            self._fill_first_stack(self.stack1, self.stack2)

    def _fill_first_stack(self, s1, s2):
        while not s2.is_empty():
            item = s2.pop()
            s1.push(item)

    def pop(self):
        if self.stack1.is_empty():
            return None
        item = self.stack1.pop()
        self.front = self.stack1.peek()
        return item

    def peek(self):
        if self.stack1.is_empty():
            return None
        return self.stack1.peek()

    def empty(self):
        if self.front:
            return False
        return True


my_queue = MyQueue()
my_queue.push(1) # queue is: [1]
print(f"stack1 = {my_queue.stack1.array} stack2 = {my_queue.stack2.array} front = {my_queue.front}")
print(my_queue.peek()) # return 1
print(my_queue.pop()) # return 1, queue is [2]
print(f"stack1 = {my_queue.stack1.array} stack2 = {my_queue.stack2.array} front = {my_queue.front}")
print(my_queue.peek())
print(my_queue.empty()) # return false


