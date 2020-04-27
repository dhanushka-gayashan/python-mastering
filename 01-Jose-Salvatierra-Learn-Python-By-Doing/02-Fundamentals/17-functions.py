# Define Function
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

greet()


# Arguments and Parameters
car = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
}

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon")

calculate_mpg(car)


# Return values
car = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
}

def get_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg 

def get_name(car):
    name = f"{car['make']} {car['model']}"
    return name

def print_car_info(cat):
    name = get_name(car)
    mpg = get_mpg(car)
    print(f"{name} does {mpg} miles per gallon")

print_car_info(car)


# Default Parameters (Default value should be last one)
def add(x, y = 10):
    total = x + y
    return total

print(add(20, 30))

print(add(20))


# Named/Keyword Arguents (Default value should be last one)
def get_total(x, y = 10):
    total = x + y
    return total

print(get_total(y = 30, x = 40))

print(get_total(30, y = 40))

print(get_total(x = 30))


