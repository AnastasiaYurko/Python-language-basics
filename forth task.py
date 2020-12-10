number = input("Введите целое положительное число: ")
number = list(map(int, number))
counter = 1
listLength = len(number)
i = 1
maximum = int(number[0])

while counter < listLength:
    if number[i] > maximum:
        maximum = number[i]
    i += 1
    counter += 1

print(maximum)

