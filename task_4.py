my_list = input("Введите несколько чисел через пробел, периодически повторяя некоторые из них: ").split( )
my_list = list(map(int, my_list))

new_list = [el for el in my_list if my_list.count(el) < 2]

print(f"Введенный список: {my_list}")
print(f"Список элементов, не имеющих повторений: {new_list}")
