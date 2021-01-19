# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, ddmmyy):
        self.ddmmyy = ddmmyy

    @classmethod
    def day_mon_year_int(cls, ddmmyy):
        ddmmyy_list = ddmmyy.split("-")
        day = int(ddmmyy_list[0])
        month = int(ddmmyy_list[1])
        year = int(ddmmyy_list[2])
        print(f"День - {day}, Месяц - {month}, Год - {year}, Тип: {type(day), type(month), type(year)}")

    @staticmethod
    def mon_year_valid(month, year):
        if 0 < month < 13:
            print(f"Валидация прошла успешно. Ваш месяц - {month}")
            if 1950 < year < 2021:
                print(f"Валидация прошла успешно. Ваш год - {year}")
            else:
                raise ValueError
        else:
            raise ValueError


dmy = Data("15-08-21")
print(dmy.day_mon_year_int("15-08-21"))
print(dmy.mon_year_valid(12, 2020))
print(dmy.mon_year_valid(11, 21))
