class Car:
    def __init__(self, speed, color,  name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going'. format(self. name))
    def stop(self):
        print('{} is stopping'.format(self.name))
    def stop(self, direction):
        print('{} is turning'.format(self.name, direction))
    def show_speed(self):
        print('Current speed', (self.speed))

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы превысили скорость!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('Current speed', (self.speed))
        if self.speed > 40:
            print('Вы превысили скорость!')

class PoliceCar(Car):
    pass

sport_car = SportCar(220, 'Синий', 'Спорткар', False)
town_car = TownCar(120, 'Белый', 'Городской автомобиль', False)
work_car = WorkCar(100, 'Серый','Рабочий автомобиль', False)
police_car = PoliceCar(170, 'Красный', 'Полицейский автомобиль', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')