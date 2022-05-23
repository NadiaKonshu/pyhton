from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self):
            self.color = (('Red', 7), ('Yellow', 2), ('Green', 3))

    def running(self):
        for color, sec in cycle(self.color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)

traffic_light = TrafficLight()
traffic_light.running()