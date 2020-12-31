amount = int(input("Введите количество товаров: "))
counter = 0
database = []
goods = []
prices = []
quantity_2 = []
units = []

while counter < amount:
    counter += 1
    t = tuple(str(counter))
    system = ["Название", "Цена", "Количество", "Ед. изм."]

    good = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    unit = input("Введите единицу измерения: ")

    information = []
    information.append(good)
    information.append(price)
    information.append(quantity)
    information.append(unit)

    d = dict(zip(system, information))
    part = t + (d, )
    database.append(part)

    goods.append(good)
    prices.append(price)
    quantity_2.append(quantity)
    units.append(unit)

    analytics = dict(zip(system, [goods, prices, quantity_2, units]))

print(database)
print(analytics)
