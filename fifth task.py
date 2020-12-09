revenue = int(input("Введите размер выручки фирмы: "))
costs = int(input("Введите размер убытков фирмы: "))
profit = revenue - costs

if revenue > costs:
    print("Ваша выручка больше, чем издержки. Деятельность Вашей фирмы приносит прибыль")
    efficiency = round(((revenue / profit) / 100), 2)
    print(f"Рентабельность Вашей выручки составляет {efficiency}%")
    employees = int(input("Введите численность сотрудников: "))
    profitforemp = int(profit / employees)
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет {profitforemp}")
else:
    print("К сожалению, издержки больше выручки. Ваша фирма находится в убытке")


