my_list = input("Введите значения списка через пробел: ").split( )
n = len(my_list)-1

for i in range(0, n, 2):
    my_list[i], my_list[i + 1] = my_list[i+1], my_list[i]

print(my_list)
