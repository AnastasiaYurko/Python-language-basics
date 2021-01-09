class Stationery:
    def __init__(self, title='канцелярия'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self, width):
        print(f'Толщина ручки {width}, отрисовка займет 1ч')


class Pencil(Stationery):
    def draw(self, soft):
        print(f'Мягкость карандаша {soft}, отрисовка займет 40 мин')


class Handle(Stationery):
    def draw(self, color):
        print(f'Вы выбрали {color} цвет. Запуск отрисовки')


tassel = Stationery()
tassel.draw()

parker = Pen()
parker.draw(0.5)

forum = Pencil()
forum.draw('HB')

marker = Handle()
marker.draw('синий')
