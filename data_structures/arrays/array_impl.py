class MyArray:
    def __init__(self):
        self._arr = dict()
        self._length = 0

    def __str__(self):
        return str(self.__dict__)

    @property
    def length(self):
        return self._length

    def lookup(self, index):
        if index >= self._length:
            raise IndexError("list index out of range")
        return self._arr[index]

    def push(self, element):
        self._arr[self._length] = element
        self._length += 1

    def pop(self):
        if self._length > 0:
            element = self._arr[self._length - 1]
            del self._arr[self._length - 1]
            self._length -= 1
            return element
        return None

    def insert(self, index, element):
        if index <= self._length:
            for i in range(self._length, index, -1):
                self._arr[i] = self._arr[i-1]
            self._arr[index] = element
            self._length += 1
            return element
        return None

    def search(self, element):
        for i in range(self._length):
            if self._arr[i] == element:
                return i
        return None

    def delete(self, index):
        if index < self._length:
            element = self._arr[index]
            for i in range(index, self._length-1):
                self._arr[i] = self._arr[i+1]
            del self._arr[self._length-1]
            self._length -= 1
            return element
        return None


if __name__ == "__main__":
    array = MyArray()
    print(array)
    print(f"length = {array.length}")

    print("Test push")
    print("array.push(1)")
    array.push(1)
    print("array.push(2)")
    array.push(2)
    print("array.push(3)")
    array.push(3)
    print("array.push(4)")
    array.push(4)
    print(array)
    print(f"length = {array.length}")

    print("Test pop")
    print("array.pop()")
    array.pop()
    print(array)
    print(f"length = {array.length}")
    print("array.pop()")
    array.pop()
    print(array)
    print(f"length = {array.length}")

    print("Test get/lookup")
    print(f"array.lookup(0) = {array.lookup(0)}")
    print(f"array.lookup(1) = {array.lookup(1)}")

    print("Test insert")
    print("array.insert(0, 0)")
    array.insert(0, 0)
    print(array)
    print(f"length = {array.length}")
    print("array.insert(2, 3)")
    array.insert(2, 3)
    print(array)
    print(f"length = {array.length}")
    print("array.insert(array.length, 7)")
    array.insert(array.length, 7)
    print(array)
    print(f"length = {array.length}")

    print("Test delete")
    print("array.delete(0)")
    array.delete(0)
    print(array)
    print(f"length = {array.length}")

    print("array.delete(2)")
    array.delete(2)
    print(array)
    print(f"length = {array.length}")

    print("array.delete(array.length-1)")
    array.delete(array.length - 1)
    print(array)
    print(f"length = {array.length}")
