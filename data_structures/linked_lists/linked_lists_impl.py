# Linked lists are, as the name suggests, a list which is linked.
# It consists of nodes which contain data and a pointer to the next node in the list.
# The list is connected with the help of these pointers.
# These nodes are scattered in memory, quite like the buckets in a hash table.
# The node where the list starts is called the head of the list
# and the node where it ends, or last node, is called the tail of the list.
# The average time complexity of some operations involving linked lists are as follows:

# Look-up   -   O(n)
# Insert    -   O(n)
# Delete    -   O(n)
# Append    -   O(1)
# Prepend   -   O(1)

# Python doesn't have a built-in implementation of linked lists, we have to build it on our own
# So, here we go.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.__dict__)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self._length = 0

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
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self._length = +1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self._length += 1

    def prepend(self, value):
        # add to the beginning
        new_node = Node(value)
        if self.head is None:
            self.append(value)
        else:
            new_node.next = self.head
            self.head = new_node
            self._length += 1

    def insert(self, index, value):
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
        new_node.next = leader.next
        leader.next = new_node
        self._length += 1

    def _travesre_to_index(self, index):
        # check params
        cur_node = self.head
        for _ in range(index):
            cur_node = cur_node.next
        return cur_node

    def find_by_value(self, value):  # Time Complexity - O(n)
        """
        Find and return the first node with specific value in Linked List
        :param value: value to find
        :return: node
        """
        current_node = self.head
        while current_node:
            # will work only with hash table class
            # because value have to contain array with 2 params [key, value]
            if current_node.value[0] == value:
                return current_node
            current_node = current_node.next
        return None

    def remove(self, index):
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

        leader = self._travesre_to_index(index-1)
        leader.next = leader.next.next
        if not leader.next:
            self.tail = leader
        self._length -= 1

    def get_values(self):
        if self.head is None:
            return None
        array = []
        current_node = self.head
        while current_node:
            array.append(current_node.value)
            current_node = current_node.next
        return array

    def reverse(self):
        # Time complexity - O(n)
        # Space complexity - O(n)
        array = []
        cur_node = self.head
        while cur_node:
            array.append(cur_node.value)
            cur_node = cur_node.next
        array.reverse()
        if len(array) > 1:
            self.__init__()
            self.append(array[0])
            for i in range(1, len(array)):
                self.append(array[i])

    def reverse2(self):
        if self._length <= 1:
            return self.head
        # Update the tail of the list to point to the head
        # as after reversing the present head will become the last node
        self.tail = self.head
        # Create two nodes first and second
        # which point to the first and second nodes of the list respectively.
        first = self.head
        second = first.next
        # Run a loop until second becomes None
        while second:
            # Inside the loop create a temporary node which points to the 'next' of the second node (third node)
            temp = second.next
            # Update the 'next' of the second node to point to the first node so that the link is now reversed
            # (second node points to first node instead of 3rd).
            second.next = first
            # Then update the first and second nodes to be equal to the second and temporary nodes respectively.
            first = second
            second = temp
        self.head.next = None
        self.head = first




my_linked_list = LinkedList()
my_linked_list.append(10)
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
my_linked_list.reverse()
print(my_linked_list)
my_linked_list.reverse2()
print(my_linked_list)
