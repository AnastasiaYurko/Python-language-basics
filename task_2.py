my_list = input("Введите нескоко чисел через пробел: ").split()
my_list = list(map(int, my_list))
index = [i for i in range(1, len(my_list) + 1)]

new_list = [el for index, el in enumerate(my_list) if my_list[index - 1] < my_list[index]]
print(f"Ваш список: {my_list}")
print(f"Список элементов исходного списка, значения которых больше предыдущего элемента: {new_list}")
