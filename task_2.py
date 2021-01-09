class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        print(self._length * self._width * 25 * 5)


road = Road(15, 50)
road.asphalt_mass()
