with open("numbers.txt", "w", encoding="UTF-8") as numbers:
    number = input("Введите числа через пробел: ")
    numbers.writelines(number)

    list_num = list(map(int, number.split( )))
    print(f"Сумма введенных чисел равна {sum(list_num)}")
