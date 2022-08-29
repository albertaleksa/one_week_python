# Google Question
# Given an array, return the first recurring character
# Example1 : array = [2,1,4,2,6,5,1,4]
# It should return 2
# Example 2 : array = [2,6,4,6,1,3,8,1,2]
# It should return 6


"""
The first solution that comes to mind is brute force solution.
Using 2 nested loops:
 - outer loop: go through array using index i
 - inner loop: runs from 0 to i
 - on i-iteration check if i-element equal to any element behind it

Time complexity - O(n^2)
Space complexity - O(1)
"""
def brute_force(array):
    # check input
    if not array or len(array) < 2:
        return "undefined"
    for i in range(len(array)):
        for j in range(i):
            if array[i] == array[j]:
                return array[i]
    return None


# It's not efficient.
# Try to find more efficient solution
"""
I can create a hash map (dictionary)
Than go through array and put each element into the dictionary 
(key - element from array
 value - any value, I will store "True").
But before storing I'll check if this element is already present in the dictionary or not.
If yes, then I return this element and break out the loop
If not, then I add element into the dictionary and go ahead.

Time complexity - O(n)
Space complexity - O(n)
"""

def first_rec(array):
    # check input
    if not array or len(array) < 2:
        return None
    keys = {}
    for el in array:
        if el in keys:
            return el
        else:
            keys[el] = True
    return None


print(brute_force([2,1,4,2,6,5,1,4]))
print(brute_force([2,6,4,6,1,3,8,1,2]))

print(first_rec([2,1,4,2,6,5,1,4]))
print(first_rec([2,6,4,6,1,3,8,1,2]))
print(first_rec([2, 3, 4, 5]))
print(first_rec([]))
print(first_rec([2]))

print(brute_force([2, 5, 5, 2, 3, 5, 1, 2, 4]))
print(first_rec([2, 5, 5, 2, 3, 5, 1, 2, 4]))