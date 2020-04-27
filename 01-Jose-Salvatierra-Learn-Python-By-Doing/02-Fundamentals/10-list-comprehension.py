# Add Repeating Numbers
repate_numbers = [5 for number in range(5)]
print(repate_numbers)


# Double Numbers
numbers = [0, 1, 2, 3, 4, 5]

double_numbers = [number * 2 for number in numbers]
print(double_numbers)


# Custom String List
ages = [23, 34, 45, 56, 67]

ages_string = [f"My friend is {age} years old." for age in ages]
print(ages_string)


# String Transformation
friend = input("Enter your name:")
friend_lower = friend.lower()

friends = ["Dhanushka", "Gayashan", "Nimalka", "Chamari"]
friends_lower = [name.lower() for name in friends]

if friend_lower in friends_lower:
    print(f"{friend.title()} is one of your friends!!!")


