class MyArray:
    def __init__(self):
        self._data = {}
        self._length = 0

    def __str__(self):
        return str(self.__dict__)

    @property
    def length(self):
        return self._length

    def push(self, value):
        self._data[self._length] = value
        self._length += 1

    def pop(self):
        if self._length == 0:
            raise IndexError("list is empty")
        item = self._data[self._length-1]
        del self._data[self._length-1]
        self._length -=1
        return item

    def lookup(self, index):
        if index >= self._length:
            raise IndexError("list index out of range")
        return self._data[index]

    def insert(self, index, item):
        for i in range(self._length, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = item
        self._length += 1

    def delete(self, index):
        item = self._data[index]
        self._shift_items(index)
        del self._data[self._length-1]
        self._length -= 1
        return item

    def _shift_items(self, index):
        for i in range(index, self._length-1):
            self._data[i] = self._data[i+1]


my_array = MyArray()
print(my_array.length)
print(my_array)
my_array.push(1)
print(my_array)
my_array.push(2)
print(my_array)
my_array.insert(0, 0)
print(my_array)
my_array.insert(3, 3)
print(my_array)
print(my_array.length)
print(my_array.lookup(1))
print(my_array.delete(0))
print(my_array)