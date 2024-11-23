# 7.6
import itertools
import random

def iter_a():
    return itertools.cycle(["0,", "1,"])

def iter_b():
    while True:
        yield random.choice(["N", "E", "S", "W"])

def iter_c():
    return itertools.cycle(range(7))

if __name__ == '__main__':
    a = iter_a()
    b = iter_b()
    c = iter_c()

    print("Test iteratora a: ", end=" ")
    for _ in range(15):
        print(next(a), end=" ")
    print()

    print("Test iteratora b: ", end=" ")
    for _ in range(15):
        print(next(b), end=" ")
    print()

    print("Test iteratorb c: ", end=" ")
    for _ in range(15):
        print(next(c), end=" ")
    print()