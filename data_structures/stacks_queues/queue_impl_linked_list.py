class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        pop_node = self.first
        if not pop_node:
            return None
        if self.last == self.first:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return pop_node.value

    def peek(self):
        if self.first:
            return self.first.value
        return None


if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue("first")
    my_queue.enqueue("second")
    my_queue.enqueue("third")
    print(my_queue.peek())
    item = my_queue.dequeue()
    print(item.value)
    print(my_queue.peek())
    item = my_queue.dequeue()
    print(item.value)
    print(my_queue.peek())
    item = my_queue.dequeue()
    print(item.value)
    print(my_queue.peek())