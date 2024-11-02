# *** ZESTAW 4 ***
import math
from audioop import findfactor
from math import isinf
from pydoc_data.topics import topics
from wsgiref.validate import assert_


# Zadanie 4.2
def make_ruler(n):
    ruler = ""
    for i in range(n):
        ruler += "|...."
    ruler += "|"

    numbers = "0"
    for i in range(1, n + 1):
        numbers += str(i).rjust(5)

    ruler += "\n" + numbers
    return ruler

def make_grid(rows, cols):
    if (rows <= 0 or cols <= 0):
        print("Invalid number of rows and columns")
        return False
    square = ""
    top_wall = "+---" * cols + "+"
    side_wall = "|"
    for _ in range(cols):
        side_wall += "|".rjust(4)

    for i in range(rows * 2):
        if i % 2 == 0:
            square += top_wall + "\n"
        else:
            square += side_wall + "\n"
    square += top_wall + "\n"
    return square

# Zadanie 4.3
def factorial(n):
    assert n >= 0, "n must be greater than or equal to 0"
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Zadanie 4.4
def fibonacci(n):
    assert n >= 0, "n must be greater than or equal to 0"
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(n - 1):
        b += a
        a = b-a
    return b

# Zadanie 4.5
def odwracanie(L, left, right):
    while left < right:
        tmp = L[left]
        L[left] = L[right]
        L[right] = tmp
        left += 1
        right -= 1
    return L

def odwracanie_rekurencja(L, left, right):
    if left >= right:
        return L
    tmp = L[left]
    L[left] = L[right]
    L[right] = tmp
    return odwracanie_rekurencja(L, left+1, right-1)

# Zadanie 4.6
def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        elif isinstance(item, (int, float)):
            sum += item
    return sum

# Zadanie 4.7
def flatten(sequence):
    flatened_sequence = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flatened_sequence.extend(flatten(item))
        else:
            flatened_sequence.append(item)
    return flatened_sequence
# TESTY
def tests():
    print(make_ruler(12)) # 4.2 a
    print(make_grid(2,4)) # 4.2 b
    print(factorial(4)) # 4.3
    print(fibonacci(19)) # 4.4
    print(odwracanie([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 6)) # 4.5 a
    print(odwracanie_rekurencja([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 6)) # 4. 5 b
    print(sum_seq([1, 2, 3, [1, 2, 4], (1, 3, 4), 9, 10])) # 4.6
    print(flatten([1, 2, 3, [1, [2, 4]], [2, [3, [4, [5], 6], 7], 8, (1, 3, 4)], 9, 10]))

tests()