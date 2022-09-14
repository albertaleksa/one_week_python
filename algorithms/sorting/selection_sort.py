"""
Selection sort
involves finding the minimum element in one pass through the array
and then swapping it with the first position of the unsorted part of the array.
Time complexity     -   O(n^2) in all cases
Space complexity    -   O(1)

However, selection sort has the property of minimizing the number of swaps.
In applications where the cost of swapping items is high,
selection sort very well may be the algorithm of choice.
"""


def selection_sort(array):
    length = len(array)
    # -1 because when only 1 element remains, it will be already be sorted
    for i in range(length-1):
        # Set the index of minimum element to be the ith index
        min_index = i
        # Check the array from the i+1th element to the end
        for j in range(i+1, length):
            # If a smaller element than the minimum element is found,
            if array[j] < array[min_index]:
                # re-assign the index of the minimum element
                min_index = j
        # If min_index has changed, i.e, a smaller  element has been found,
        if i != min_index:
            # then swap that element with the ith element
            swap(array, i, min_index)


def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selection_sort(arr)
print(arr)
