# Doubly linked lists are just normal, singly linked lists with one added feature,
# a link to the previous node as well in addition to a link to the next node.
# Although the worst case time complexities of all operations
# in a doubly linked list are same as that of a singly linked list,
# Some operations are technically faster.
# For example, lookup or searching, is O(n/2) as search can begin from both ends
# But O(n/2) = O(n), so it is still the same as that for a singly linked list.

# Look-up   -   O(n)
# Insert    -   O(n)
# Delete    -   O(n)
# Append    -   O(1)
# Prepend   -   O(1)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.__dict__)


class DoublyLinkedList:
    def __init__(self, value):
        print(f"{DoublyLinkedList.__init__.__name__}({value})")
        self.head = Node(value)
        self.tail = self.head
        self._length = 1

    def __str__(self):
        if self.head is None:
            return "empty"
        array = []
        cur_node = self.head
        while cur_node:
            array.append(cur_node.value)
            cur_node = cur_node.next
        return f"{array} len={self._length} head={self.head} tail={self.tail}"

    @property
    def length(self):
        return self._length

    def append(self, value):
        # add to the end
        print(f"{DoublyLinkedList.append.__name__}({value})")
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self._length += 1

    def prepend(self, value):
        # add to the beginning
        print(f"{DoublyLinkedList.prepend.__name__}({value})")
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self._length += 1

    def insert(self, index, value):
        print(f"{DoublyLinkedList.insert.__name__}({index}, {value})")
        # check params
        if index < 0:
            print("Index can't be negative")
            return
        # if the position more than list length, then add to the end of list
        if index >= self._length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)

        new_node = Node(value)
        leader = self._travesre_to_index(index-1)
        follower = leader.next
        new_node.next = follower
        new_node.prev = leader
        leader.next = new_node
        follower.prev = new_node

        self._length += 1

    def _travesre_to_index(self, index):
        # check params
        if index < self._length / 2:
            cur_node = self.head
            for _ in range(index):
                cur_node = cur_node.next
        else:
            cur_node = self.tail
            for _ in range(self._length-index-1):
                cur_node = cur_node.prev
        return cur_node

    def remove(self, index):
        print(f"{DoublyLinkedList.remove.__name__}({index})")
        # check params
        if index < 0:
            print("Index can't be negative")
            return
        if index >= self._length:
            print("Wrong index")
            return
        if not self.head:
            print("Linked List is empty")
            return
        if index == 0:
            self.head = self.head.next
            self._length -= 1
            return

        current = self._travesre_to_index(index)
        leader = current.prev
        follower = current.next
        leader.next = follower
        if follower:
            follower.prev = leader
        else:
            self.tail = leader
        self._length -= 1



my_linked_list = DoublyLinkedList(10)
print(my_linked_list)
my_linked_list.append(5)
print(my_linked_list)
my_linked_list.append(16)
print(my_linked_list)
my_linked_list.prepend(1)
print(my_linked_list)
print("Insert")
my_linked_list.insert(2, 99)
print(my_linked_list)
my_linked_list.insert(0, 0)
print(my_linked_list)
my_linked_list.insert(1, 2)
print(my_linked_list)
print("Remove")
my_linked_list.remove(1)
print(my_linked_list)
my_linked_list.remove(5)
print(my_linked_list)
my_linked_list.remove(0)
print(my_linked_list)
my_linked_list.remove(20)
print(my_linked_list)
