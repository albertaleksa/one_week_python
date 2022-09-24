"""
Quick Sort
Quick Sort is another sorting algorithm which follows divide and conquer approach.
It requires to chose a pivot,
then place all elements smaller than the pivot on the left of the pivot
and all elements larger on the right
Then the array is partitioned in the pivot position and
the left and right arrays follow the same procedure until the base case is reached.
After each pass the pivot element occupies its correct position in the array.
Time complexity     -   O(nlog N) - Best.   Worst - O(n^2)
Space complexity    -   O(log n)
"""


def quick_sort(array, left, right):
    if left < right:
        # print(f"array = {array}     left = {left} right = {right}")
        partition_index = partition(array, left, right)
        # print(f"partition_index = {partition_index}")
        quick_sort(array, left, partition_index - 1)
        quick_sort(array, partition_index + 1, right)


def partition(array, left, right):
    # sort array in way that all elements that less than pivot are to the left to the pivot
    # and all elements that more than pivot are to the right to the pivot
    # return the pivot index
    pivot_index = choose_pivot(array, left, right)
    left_index = left
    while left_index < pivot_index:
        # print(f"left_index = {left_index} right_index = {right_index} pivot_index = {pivot_index}")
        # print(f"array = {array}")
        # if element left to the pivot is more than pivot
        if array[left_index] > array[pivot_index]:
            # put left element to the right of pivot, shift pivot one position to left
            # and put element from one position left to pivot to the left position
            swap_elements(array, left_index, pivot_index)
            pivot_index -= 1
        else:
            left_index += 1
    return pivot_index


def swap_elements(array, left_index, pivot_index):
    # then on left_index place put element which is one position left to pivot
    temp = array[left_index]
    array[left_index] = array[pivot_index - 1]
    # shift pivot element to one position left
    array[pivot_index - 1] = array[pivot_index]
    # put to the old pivot position element from old left_index
    array[pivot_index] = temp

def choose_pivot(array, left, right):
    """
    Take the last element of the array as a pivot
    :param array:
    :param left:
    :param right:
    :return:
    """
    return right


number = [3, 7, 8, 5, 2, 1, 9, 5, 4]
number2 = [0, 99, 44, 6, 2, 99, 1, 5, 63, 63, 87, 283, 4, 0, 0]
number3 = [6, 5, 3, 1, 8, 7, 2, 4]
print(number)
quick_sort(number, 0, len(number) - 1)
print(number)

print(number2)
quick_sort(number2, 0, len(number2) - 1)
print(number2)

print(number3)
quick_sort(number3, 0, len(number3) - 1)
print(number3)