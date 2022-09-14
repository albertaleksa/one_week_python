"""
In Bubble Sort,
the largest value is bubbled up in every pass.
Every two adjacent items are compared and
they are swapped if they are in the wrong order.
This way, after every pass,
the largest element reaches to the end of the array.
Time complexity     -   O(n^2) (in Worst and Average Case),    O(n) - in best case when data is nearly sorted
Space complexity    -   O(1)
"""


def bubble_sort(array):
    length = len(array)
    # -1 because when only 1 item will be left, we don't need to sort that
    for i in range(length-1):
        # In every iteration of the outer loop, one number gets sorted.
        # So the inner loop will run only for the unsorted part
        for j in range(length-1-i):
            # If two adjacent elements in the wrong order are found, they are swapped
            if array[j] > array[j+1]:
                swap(array, j, j+1)


def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
bubble_sort(arr)
print(arr)