"""
Write 2 functions to find the factorial of any number.
One should use recursive, the other - just use a for loop.

Recursive Rules:
1. Identify the base case
2. Identify the recursive case
3. Get closer and closer and return when needed. Usually you have 2 returns
"""


def find_factorial_recursive(num):
    # O(n) - Time complexity
    # base case
    if num == 1:
        return 1
    # recursive case
    else:
        return num * find_factorial_recursive(num-1)


def find_factorial_iterative(num):
    # O(n) - Time complexity
    result = 1
    for i in range(2, num+1):
        result *= i
    return result


print(find_factorial_recursive(6))
print(find_factorial_iterative(6))

