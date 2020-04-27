class Dog:

    dogInfo = 'Dogs are cool...'

    def bark(self):
        print('BARK!!!!')


mydog = Dog()
mydog.bark()

mydog.name = 'Fido'
print(mydog.name)

mydog.age = 12
print(mydog.age)

print(Dog.dogInfo)


class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def details(self):
        return f"{self.model} is {self.color} color"


myCar = Car('BMW X5', 'Black')

print(myCar.model)

print(myCar.color)

print(myCar.details())
