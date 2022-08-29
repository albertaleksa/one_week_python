def merge_sorted_arrays(arr1, arr2):
    # Time complexity of this solution is O(n+m)
    # Space complexity - O(n+m)
    # check input
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    if arr1 is None or arr2 is None:
        return "Wrong input"
    lst = []
    ind1, ind2 = 0, 0
    # The loop runs until I reach the end of one of the arrays
    while ind1 < len(arr1) and ind2 < len(arr2):
        if arr1[ind1] <= arr2[ind2]:
            lst.append(arr1[ind1])
            ind1 += 1
        else:
            lst.append(arr2[ind2])
            ind2 += 1

    # If one of the array's end wasn't reached I should add the remaining elements to the new array
    lst.extend(arr1[ind1:])
    lst.extend(arr2[ind2:])

    return lst


print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
