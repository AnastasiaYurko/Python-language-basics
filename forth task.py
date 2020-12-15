words = input("Введиет несколько слов, разделяя их пробелами: ").split( )
counter = 0

for i in words:
    counter += 1
    if len(list(i)) > 10:
        long = list(i[0:10])
        word = "".join(long)
        print(f"{counter}. {word}")
    else:
        print(f"{counter}. {i}")
