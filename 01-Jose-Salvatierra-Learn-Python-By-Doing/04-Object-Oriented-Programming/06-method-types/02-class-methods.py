# Class Methods: Get Class as the first Argument
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @classmethod
    def get_class(cls):
        return 'Class is {cls.__name__}'


dhanu = Student("Dhanushka", "UAT")

print(dhanu.get_class())
