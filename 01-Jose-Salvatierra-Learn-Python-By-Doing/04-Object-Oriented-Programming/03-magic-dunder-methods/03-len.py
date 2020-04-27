# Implement Dunder "Len" Method

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)


ford = Garage()

ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford))
