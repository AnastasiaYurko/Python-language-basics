from itertools import count

a = int(input("Введите число, с которого начнется счет: "))
b = int(input("Введите число, на котором счет остановится: "))

for el in count(a):
    if el > b:
        break
    print(el)
