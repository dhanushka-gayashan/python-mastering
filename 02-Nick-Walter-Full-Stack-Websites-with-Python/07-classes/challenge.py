from datetime import date

class Car:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return date.today().year - self.year


myCar = Car(2019, 'BMW', 'X5')

print(myCar.age())
