# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} едет с превышением скорости на {self.speed - 60} км/ч')
        print(f'{self.name} едет со скоростью {self.speed} км/ч')


class SportCar(Car):
    def acceleration(self):
        accel = self.speed * 3 / 100
        print(f'{self.name} разгонится до {self.speed} за {accel}с')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} едет с превышением скорости на {self.speed - 40} км/ч')
        print(f'{self.name} едет со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    def viu_viu(self):
        print('Виу-виу *мигает лампочками*')


car_1 = Car(80, 'черный', 'Audi')
print(f'Имя: {car_1.name}')
print(f'Скорость: {car_1.speed}')
print(f'Цвет: {car_1.color}')
print(f'Полицейская? {car_1.is_police}')
car_1.go()
car_1.turn("направо")
car_1.show_speed()
car_1.stop()

car_town = TownCar(70, 'красный', 'Toyota')
print(f'Имя: {car_town.name}')
print(f'Скорость: {car_town.speed}')
print(f'Цвет: {car_town.color}')
print(f'Полицейская? {car_town.is_police}')
car_town.go()
car_town.turn("направо")
car_town.show_speed()
car_town.stop()

car_sport = SportCar(120, 'желтый', 'Porsche')
print(f'Имя: {car_sport.name}')
print(f'Скорость: {car_sport.speed}')
print(f'Цвет: {car_sport.color}')
print(f'Полицейская? {car_sport.is_police}')
car_sport.go()
car_sport.turn("налево")
car_sport.show_speed()
car_sport.acceleration()
car_sport.stop()

car_work = WorkCar(60, 'черный', 'Chevrolet')
print(f'Имя: {car_work.name}')
print(f'Скорость: {car_work.speed}')
print(f'Цвет: {car_work.color}')
print(f'Полицейская? {car_work.is_police}')
car_work.go()
car_work.turn("направо")
car_work.show_speed()
car_work.stop()

police = PoliceCar(150, 'бело-синий', 'Mazda', True)
print(f'Имя: {police.name}')
print(f'Скорость: {police.speed}')
print(f'Цвет: {police.color}')
print(f'Полицейская? {police.is_police}')
police.go()
police.turn("направо")
police.show_speed()
police.stop()
police.viu_viu()

