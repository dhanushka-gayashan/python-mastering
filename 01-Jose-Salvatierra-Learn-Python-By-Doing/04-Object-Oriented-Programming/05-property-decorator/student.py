# @Property : Convert "no argument" methods into a Property
# Use for Properties like do Calculations.

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @property
    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 40


dhanu = WorkingStudent("Dhanushka", "UAT", 16.0)

dhanu.marks.append(95)
dhanu.marks.append(81)
dhanu.marks.append(78)
dhanu.marks.append(88)

print(dhanu.name)
print(dhanu.school)
print(dhanu.salary)

print(dhanu.average)

print(dhanu.weekly_salary)
