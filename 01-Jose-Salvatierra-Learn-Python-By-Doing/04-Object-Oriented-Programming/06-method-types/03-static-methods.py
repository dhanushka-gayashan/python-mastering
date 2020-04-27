# Static Methods: Do not get any Argument
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @staticmethod
    def greet():
        return 'Hello there...'


dhanu = Student("Dhanushka", "UAT")

print(dhanu.greet())

