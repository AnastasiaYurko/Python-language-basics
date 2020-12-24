from itertools import cycle

user_list = input("Введите несколько слов через пробел: ").split( )
stop = int(input("Сколько перемещений по итератору Вы хотите выполнить? "))
rep = cycle(user_list)
counter = 0

for el in cycle(rep):
    if counter >= stop:
        break
    print(next(rep))
    counter += 1

# не понимаю, почему идет скачок через элемент
