class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Оклад': 30000, 'Премия': 10000}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход сотрудника с учетом премии равен {sum(self._income.values())}р')


worker_1 = Position("Иван", "Петров", "бухгалтер")
print(f'Имя {worker_1.name}')
print(f'Должность {worker_1.position}')
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position("Максим", "Ивушкин", "юрист")
print(f'Имя {worker_2.name}')
print(f'Должность {worker_2.position}')
worker_2.get_full_name()
worker_2.get_total_income()
