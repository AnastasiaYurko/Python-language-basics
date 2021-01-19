class NilDivErr(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = int(input("Введите делимое: "))
divider = int(input("Введите делитель: "))

try:
    if divider == 0:
        raise NilDivErr("Нельзя делить на 0!")
except NilDivErr as err:
    print(err)
else:
    res = dividend / divider
    print(f"Резултат деления: {res}")