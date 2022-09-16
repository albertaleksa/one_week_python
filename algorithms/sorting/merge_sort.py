"""
Merge Sort
uses the Divide and Conquer approach.
It involves breaking up the array from the middle until
Arrays of only 1 elements remain and then merging them back up in a sorted order.
Time complexity     -   O(nlog N)
Space complexity    -   O(n)
"""

def merge_sort(array):
    length = len(array)
    # base case to stop recursion
    if length == 1:
        return array
    # split array in into right and left
    middle = length // 2
    left_array = array[:middle]
    right_array = array[middle:]
    return merge(merge_sort(left_array),
                 merge_sort(right_array))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    # go through 2 sorted arrays: left and right
    # and compare elements and put elements from those 2 arrays in new array in sorted way
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # add in result array existing elements from left array
    if left_index < len(left):
        result.extend(left[left_index:])
    # add in result array existing elements from right array
    if right_index < len(right):
        result.extend(right[right_index:])
    return result


number = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# number = [6, 5, 3, 1, 8, 7, 2, 4]
print(number)
print(merge_sort(number))
