from itertools import count
from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


f = int(input("Введите число: "))

print(f"Факториалы чисел от 1 до {f}: ")

for i in fact(f):
    print(i)
