# Truthy and Falsy 
truthy = True 
falsy = False 


# Boolena Comparison
age = 20

is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20


# AND
age = 30
can_learn_programming = age > 0 and age < 100


# OR
age = 30
usually_working = age >= 18 or age <= 65


# bool() - Convert into boolean
print(bool(35))
print(bool(0))

print(bool("Dhanushka"))
print(bool(""))


# Usage AND and OR
x = 35 and 0
print(x)

x = 0 and 35
print(x)

x = True and 18
print(x)

x = 35 or 0
print(x)

x = 0 or 35
print(x)

x = False or 35
print(x)

age = 16
side_job = True 
print(age > 18 and age < 65 or side_job) # Eveluate Left to Right

name = input("Enter your name: ")
surname = input("Enter your suername: ")
greeting = name or f"Mr. {surname}"
print(greeting)


# Use of NOT
x = not False
print(x)

x = not True
print(x)

x = not 35
print(x)

x = not 0
print(x)
