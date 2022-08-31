from data_structures.linked_lists.linked_lists_impl import Node, LinkedList


class HashTable:
    """
    Hash tables are pre-defined in Python in the form of dictionaries.
    Implement our own Hash Table.
    Here, we will implement our own hash table with some common methods such as
    set, get, remove, keys, values
    """
    def __init__(self, size):
        # We initialize the size of our hash table(no. of buckets) with the size given to the class object
        self._size = size
        # We initialize an array of size 'size' with None
        self._data = [None] * self._size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        # Time Complexity - O(1)
        """
        Our custom hash function
        :param key: hash table key
        :return: number between 0..size
        """
        my_hash = 0
        for i in range(len(key)):
            # ord(key[i]) gives the unicode code point of the character key[i]
            my_hash = (my_hash + ord(key[i]) * i) % self._size
        # The hash value obtained after applying the hash function to the key is returned
        return my_hash

    def test_hash(self):
        self._hash("abcdefghi")

    def get_old(self, key):
        # Time Complexity - O(1). When collision and bad hash function - O(n)
        # Hash value of the key is calculated by passing the key to the _hash function
        index = self._hash(key)
        current_bucket = self._data[index]
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None

    def get(self, key):
        # Time Complexity - O(1). When collision and bad hash function - O(n)
        # Hash value of the key is calculated by passing the key to the _hash function
        index = self._hash(key)
        current_bucket = self._data[index]
        if current_bucket:
            return current_bucket.find_by_value(key).value
        return None

    def set_old(self, key, value):
        # Time Complexity - O(1). When collision and bad hash function - O(n)
        # Hash value of the key is calculated by passing the key to the _hash function
        index = self._hash(key)
        # If the 'hash' position of the data array is empty, we create a new empty array
        if not self._data[index]:
            self._data[index] = []
        # If the 'hash' position is not empty, implying a collision,
        # we simply append the list of key,value pair to the lists already present
        # When key is already exists in Hash Table, then rewrite value
        for i in range(len(self._data[index])):
            if self._data[index][i][0] == key:
                self._data[index][i][1] = value
                return None
        self._data[index].append([key, value])

    def set(self, key, value):
        # Time Complexity - O(1). When collision and bad hash function - O(n)
        # Hash value of the key is calculated by passing the key to the _hash function
        index = self._hash(key)
        # If the 'hash' position of the data array is empty, we create a new empty array
        if not self._data[index]:
            self._data[index] = LinkedList()
        # If the 'hash' position is not empty, implying a collision,
        # we simply append the list of key,value pair to the lists already present
        # When key is already exists in Hash Table, then rewrite value
        node = self._data[index].find_by_value(key)
        if node:
            node.value = [key, value]
            return None
        self._data[index].append([key, value])

    def remove(self, key):
        pass

    def keys(self):
        keys_array = []
        for el in self._data:
            if el:
                if el.length > 0:
                    values = el.get_values()
                    for inner_el in values:
                        keys_array.append(inner_el[0])
        return keys_array

    def values(self):
        values_array = []
        for i in range(self._size):
            current_bucket = self._data[i]
            if current_bucket:
                if current_bucket.length > 0:
                    values = current_bucket.get_values()
                    for el in values:
                        values_array.append(el[1])
        return values_array



my_hash_table = HashTable(5)
print(my_hash_table)

my_hash_table.test_hash()

my_hash_table.set('grapes', 10000)
my_hash_table.set('oranges', 5)
my_hash_table.set('bananas', 123)
my_hash_table.set('carrot', 34)
my_hash_table.set('melon', 2)
my_hash_table.set('tomatoes', 7)
print(my_hash_table)
my_hash_table.get('grapes')
print(my_hash_table)

print(my_hash_table.keys())
print(my_hash_table.values())

