# IF Statement
friend = "Dhanushka"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend")
    print("Welcome to party")


# IF - ELSE Statement 
friend = "Dhanushka"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend")
    print("Welcome to party")
else:
    print("Hello, stranger")
    print("Please go away")


# Bool Values
if 5:
    print("This going to run....")


user_name = input("Enter your name: ")
if user_name:
   print("You have a name.....")     


# IN Keyword
firends = ["Dhanushka", "Gayashan"]

user_name = input("Enter your name: ")

if user_name in friend:
    print("Hello, friend!!")


# Check Values in Dictionary
my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}

do_i_know = 'Anne'

if do_i_know in my_friends:
  print(f'I know {do_i_know}')


# IF ELIF ELSE Statements
firends = ["Dhanushka", "Gayashan"]
family = ["Chamari", "Nimalka"]

user_name = input("Enter your name: ")

if user_name in friend:
    print("Hello, friend!!")
elif user_name in family:
    print("Hello, family!!")
else:
    print("I don't know you.")


# IS Keywoad
is_programmer = False

if is_programmer is False:
    print("This is going to run...")
