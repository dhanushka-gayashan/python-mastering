# Instance Methods: Get Object as the first Argument
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


dhanu = Student("Dhanushka", "UAT")

dhanu.marks.append(95)
dhanu.marks.append(81)
dhanu.marks.append(78)
dhanu.marks.append(88)

print(dhanu.average())
