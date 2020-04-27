# Implement Dunder "Represent" Method

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'


ford = Garage()

ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford)
