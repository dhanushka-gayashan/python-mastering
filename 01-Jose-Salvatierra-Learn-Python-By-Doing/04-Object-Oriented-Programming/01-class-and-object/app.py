# Define Class
class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)

    def get_address(self, address):
        return "f{self.name} lives in {address}"

# Create Object
student_one = Student("Dhanushka Gayashan", [70, 80, 90, 100])


# Get Object created Class
print(student_one.__class__)


# Access Properties 
print(student_one.name)
print(student_one.grades)


# Call Methods
average = student_one.average()
print(average)

average = Student.average(student_one)
print(average)


# Pass Multiple Arguments
lives_in = student_one.get_address("Auckland")
print(lives_in)
