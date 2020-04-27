# Index Error
friends = ["Dhanushka", "Gayashan"]
friends[2]


# Key Error
movie = {
    "name": "Metrix",
    "year": "1994"
}
movie["release"]


# Name Error
## print(hello)


# Attribute Error
friends = ["Dhanushka", "Gayashan", "Chamari"]
near_by = ["Gayashan", "Nimalka"]
## firends.intersection(near_by)  ## attribute "intersection" availbe for "Sets"


# Not Implemented Error
class User:
    def __init__(self, username, password):
      self.username = username
      self.password = password

    def login(self):
        raise NotImplementedError('This feature has been not implemented yet ..')


# Runtime Error
## Happening when run application


# Syntax Error
# class User ## Missing ":"
#     def __init__(self, name):
#         self.name = name


# Indentation Error
# def add_two(z, y):
#     pass
# return z + y


# Tab Error 
def add_two(z, y):
  return z + y

def multi_two(z, y):
    return z * y


# Type  Error
result = 5 + 'hi'


# Value Error
amount = int('20.5')


# Import Error
## Circular Imports 
### File A Import File B
### File B Import File A


# Deprecation Error
class Member:
    def __init__(self, username, password):
      self.username = username
      self.password = password

    def register(self):
        print("Member has been registerd")
        raise DeprecationWarning("This method already depricated")

    @classmethod
    def register_member(cls, username, password):
        return (f'Member has been registerd')


# UnboundLocalError: local variable 'n' referenced before assignment
def power_of_two(number):
    try:
        n = float(number)
    except ValueError:
        print('Your input was invalid.')
    finally:
        n_square = n ** 2
        return n_square

power_of_two('Dhanushka')
