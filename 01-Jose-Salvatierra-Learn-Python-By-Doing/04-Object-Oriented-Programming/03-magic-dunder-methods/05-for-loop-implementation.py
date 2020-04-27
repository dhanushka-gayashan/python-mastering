# For-Loop need "Get Item" Method in Object

class Garage:
    def __init__(self):
        self.cars = []

    def __getitem__(self, i):
        return self.cars[i]


ford = Garage()

ford.cars.append('Fiesta')
ford.cars.append('Focus')

for car in ford:
    print(car)
