def hello():
    print('Hello Python World...')


hello()


def say_name(name):
    print(f"Hello {name}...")


say_name('Dhanushka')


def say_something(name, age):
    print(f"{name} is {age} years old")


say_something('Dhanushka', 33)


def about_me(name, age=30):
    print(f"{name} is {age} years old")


about_me('Dhanushka')


def who_is_this(name, age):
    return f"{name} is {age} years old"


print(who_is_this('Dhanushka', 33))

