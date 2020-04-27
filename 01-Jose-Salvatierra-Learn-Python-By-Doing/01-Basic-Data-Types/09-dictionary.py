# Define
friend_ages = {
    "Dhanushka": 33,
    "Gayashan": 32,
    "Nimalka": 33
}

print(friend_ages)


# Get Values
friend_ages = {
    "Dhanushka": 33,
    "Gayashan": 32,
    "Nimalka": 33
}

print(friend_ages["Dhanushka"])


# Add Keys
friend_ages = {
    "Dhanushka": 33,
    "Gayashan": 32,
    "Nimalka": 33
}

friend_ages["Chamari"] = 32

print(friend_ages)


# Update Values
friend_ages = {
    "Dhanushka": 33,
    "Gayashan": 32,
    "Nimalka": 33
}

friend_ages["Gayashan"] = 33

print(friend_ages)


# Find a Key
friend_ages = {
    "Dhanushka": 33,
    "Gayashan": 32,
    "Nimalka": 33
}

if "Dhanushka" in friend_ages:
    print("Dhanushka is there...")


# Tuples/Lists of Dictionaries
friends = (
    {"name": "Dhanushka", "age": 33},
    {"name": 'Gayashan', "age": 32},
    {"name": "Chamari", "age": 33}
)

print(friends)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])


# Convert List of Tuples into Dictionary
friends = [("Dhanushka", 33), ("Gayashan", 32), ("Chamari", 32)]

friends_age = dict(friends)
print(friends_age)
