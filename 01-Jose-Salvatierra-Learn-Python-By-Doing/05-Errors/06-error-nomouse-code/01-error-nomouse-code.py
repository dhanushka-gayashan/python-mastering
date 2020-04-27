# Version 01
def power_of_twoV1():
    n = input("Please enter a number: ")
    n_square = n ** 2
    return n_square


# Version 02
def power_of_twoV2():
    user_input = input("Please enter a number: ")
    n = float(user_input)
    n_square = n ** 2
    return n_square


# Version 03
def power_of_twoV3():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
    finally:
        n_square = n ** 2
        return n_square


# Version 04
def power_of_twoV4():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        n = 0
    else:
        n_square = n ** 2
        return n_square


# Version 05
def power_of_twoV5():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        n = 0
    else:
        n_square = n ** 2
    finally:
        return n_square


# Version 06
def power_of_twoV6():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0
    finally:
        n_square = n ** 2
        return n_square
