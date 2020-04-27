# String
my_string = 'Hello, world!!!'


# Print String
print('Hello, world!!!')


# Single vs Double Quotation
quotation = "Hello, it's me."
quotation = 'He said "You are amazing" yesterday.'


# Backslash Characters
backslash = "He said \"You are amazing! \" yesterday."


# Multi Line Strings and Comments
multi_line = """
    Hello, world.

    My name is Dhanushka. Welcome to my program.
"""


# Concatinate
name = "Dhanushka"
greeting = "Hello, " + name


# Concatinate String with Integer
age = 33
age_str = str(age)
my_age = "You are " + age_str


# String Formatting
name = "Dhanushka"
age = 33
greeting = f"{name} is {age} years old."
print(greeting)

name = "Gayashan"
print(greeting)


# String Formatting - format()
greeting = "How are you, {}"

name = "Dhanushka"
dhanu_greeting = greeting.format(name)
print(dhanu_greeting)

name = "Nimalka"
nima_greeting = greeting.format(name)
print(nima_greeting)


# String Formatting - format(param)
greeting = "How are you, {name} ?"

dhanu_greeting = greeting.format(name="Dhanushka")
print(dhanu_greeting)

name = "Nimalka"
nima_greeting = greeting.format(name=name)
print(nima_greeting)
