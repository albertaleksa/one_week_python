"""
Given a number N return the index value of Fibonacci sequence,
where the sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
Recursive Rules:
1. Identify the base case
2. Identify the recursive case
3. Get closer and closer and return when needed. Usually you have 2 returns
"""


def fibonacci_iterative_array(n):
    # O(n) - Time complexity
    # O(n) - Space complexity - creating additional array
    fibonacci = [0, 1]
    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    return fibonacci[-1]


def fibonacci_iterative(n):
    # O(n) - Time complexity
    # O(1) - Space complexity
    first = 0
    second = 1
    if n == 0:
        return first
    if n == 1:
        return second
    for i in range(n-1):
        current = first + second
        first = second
        second = current
    return current


def fibonacci_recursive(n):
    # O(2^n) - Time complexity (2 to the power of n)
    # base case
    if n < 2:
        return n
    # recursive case
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_iterative(8))
print(fibonacci_iterative_array(8))
print(fibonacci_recursive(8))
