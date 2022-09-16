"""
Insertion sort
For the first iteration we fix the first element, assuming it is at its correct position
Then we loop through the rest of the elements and insert them in their correct positions,
with respect to the already sorted part of the array
Time complexity is O(n^2) in worst case. In best - O(n), when the list is almost sort or small datasets.
Space complexity - O(1)
"""


def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        for j in range(i):
            if array[i] < array[j]:
                insert(array, j, i)
                break


def insert(arr, ind1, ind2):
    temp = arr[ind2]
    for i in range(ind2, ind1, -1):
        arr[i] = arr[i-1]
    arr[ind1] = temp


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertion_sort(arr)
print(arr)