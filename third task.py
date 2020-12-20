def my_func(a, b, c):
    if a >= b >= c:
        res = a + b
    elif a >= c >= b:
        res = a + c
    else:
        res = b + c
    return res


number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третье число: "))

result = my_func(number_1, number_2, number_3)

print(f"Сумма двух наибольших чисел равна {result}")
