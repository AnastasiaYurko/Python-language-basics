class NotIntError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []
print('Для завершения программы введите "esc"')

while True:
    for_list = input("Введите элемент списка: ")
    if for_list != "esc":
        try:
            if not for_list.isdigit():
                raise NotIntError("Вы ввели не число!")
        except NotIntError as err:
            print(err)
        else:
            user_list.append(for_list)
    else:
        print("Программа завершена")
        break

print(f"Ваш список: {user_list}")
