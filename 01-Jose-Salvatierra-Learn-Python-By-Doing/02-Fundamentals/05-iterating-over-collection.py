# Iterate through List
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]

for friend in friends:
    print(friend)


# Iterate through Tuple
friends = ("Dhanushka", "Gayashan", "Chamari", "Nimalka")

for friend in friends:
    print(friend)


# Iterate through Set
friends = {"Dhanushka", "Gayashan", "Chamari", "Nimalka"}

for friend in friends:
    print(friend)


# Iterate through List of Dictionary
students = [
    {"name": "Dhanushka", "grade": 90},
    {"name": "Gayashan", "grade": 91},
    {"name": "Chamari", "grade": 92},
    {"name": "Nimalka", "grade": 93},
]

for student in students:
  name = student["name"]
  grade = student["grade"]

  print(f"{name} has a grade of {grade}.")

  
# Iterate through Dictionary
friends = {"Dhanushka": 33, "Gayashan": 32, "Chamari": 31, "Nimalka": 30}

for name in friends:  # Print Keys
    print(name)

for age in friends.values():  # Print Values
    print(age)

for name, age in friends.items():  # Print Items
    print(f"{name} is {age} years old..")
