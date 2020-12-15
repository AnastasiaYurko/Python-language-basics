month = int(input("Введите порядковый номер месяца: "))

year = ["Январь", "Февраль", "Март",
        "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь",
        "Октябрь", "Ноябрь", "Декабрь"]

if month < 3 or month == 12:
    season = "Зима"
elif month < 6:
    season = "Весна"
elif month < 9:
    season = "Лето"
else:
    season = "Осень"

print(f"Ваш месяц - {year[month-1]}. Время года - {season}")
