def num_sum():
    amount = 0
    esc = False

    while not esc:
        numbers = input("Введите числа через пробел. Для подсчета суммы нажмите Enter. Для выхода нажмите Q").split()
        res = 0

        for i in range(len(numbers)):
            if numbers[i] == 'q' or numbers[i] == 'Q':
                esc = True
                break
            else:
                res += float(numbers[i])
        amount += res
        print(f"Сумма чисел на данный момент равна {amount}")
    print(f"Конечная сумма чисел равна {amount}")


num_sum()
