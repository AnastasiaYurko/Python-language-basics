import time


def timer(sec):
    now = time.time()
    future = now + sec
    while time.time() < future:
        pass


class TrafficLight:
    def __init__(self):
        self.color = ['красный', 'желтый', 'зеленый']

    def running(self):
        c = 0
        while c < 3:
            print(f'Горит {self.color[c]} свет')

            if c == 0:
                timer(7)
                c += 1
            elif c == 1:
                timer(2)
                c += 1
            else:
                timer(10)
                c += 1


traffic_light = TrafficLight()
traffic_light.running()
