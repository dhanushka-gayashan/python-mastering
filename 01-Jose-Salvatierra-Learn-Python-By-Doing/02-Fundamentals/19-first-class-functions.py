# First Class Function: Function which can be passes as an argument into another function 
# Higher Order Function: Function which accept another Function as a parameter value

# Assing Function into a Variable
def greet():
    print("Hello!!")

hello = greet
hello()


# Pass Function as Argument 
students = [
    {"name": "Dhanushka", "grades": [85, 76, 68, 90]},
    {"name": "Gayashan", "grades": [79, 61, 82, 93]},
    {"name": "Chamari", "grades": [94, 88, 79, 69]},
    {"name": "Nimalka", "grades": [89, 78, 99, 81]},
]

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": sum,
    "top": max
}

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")
    print(operations[operation](grades))


# Usage
def over_age(data, getter):
    return getter(data) >= 18

user = {'username': 'rolf123', 'age': '35'}

print(over_age(user, lambda x: int(x['age'])))
