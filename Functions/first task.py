def division(divident, divider):
    if divider == 0:
        quotient = "Ошибка. На 0 делить нельзя!"
    else:
        quotient = round(divident / divider, 2)
    return quotient


a = int(input("Введите значение делимого: "))
b = int(input("Введите значение делителя: "))

result = division(a, b)
print(f"Результат деления: {result}")
