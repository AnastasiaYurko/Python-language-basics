number = input("Введите целое положительное число: ")
number = list(map(int, number))
counter = 1
listLength = len(number)
i = 1
max = int(number[0])

while counter < listLength:
    if number[i] > max:
        max = number[i]
        i += 1
        counter += 1
    else:
        i += 1
        counter += 1
print(max)

