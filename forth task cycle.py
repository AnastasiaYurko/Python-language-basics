def degree(x, y):
    if x < 0:
        x = int(input("Вы ввели отрицательное число. Х должен быть положительным. Попробйте еще: "))
        if y > 0:
            y = int(input("Y должен быть отрицательным числом. Попробуйте еще раз: "))
    elif y > 0:
            y = int(input("Y должен быть отрицательным числом. Попробуйте еще раз: "))
    counter = 1
    degr = 1
    while counter <= abs(y):
        counter += 1
        degr *= x
    return 1/degr


first = int(input("Введите действительное положительное число x: "))
second = int(input("Введите целое отрицательное число у: "))

result = degree(first, second)

print(f"Результат возведения числа x в степень y равен {result}")
