counter = 0
my_list = [6, 4, 2]
print(f"Первоначальный набор чисел для составления рейтинга: {my_list}")
ending = int(input("Сколько чисел вы хотите добавить в рейтинг?"))

while counter < ending:
    counter += 1
    number = int(input("Введите число: "))
    amount = my_list.count(number)
    for el in my_list:
        if amount > 0:
            i = my_list.index(number)
            my_list.insert(i + amount, number)
            break
        else:
            if number > el:
                j = my_list.index(el)
                my_list.insert(j, number)
                break
            elif number < my_list[len(my_list) - 1]:
                my_list.append(number)
print(f"Рейтинг: {my_list}")
