# Traditional way to get Index from List
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
index = 0
for friend in friends:
    print(f"{index} - {friend}")
    index = index + 1


# Use Enumerate Function to get Index from List
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
for index, friend in enumerate(friends):
    print(f"{index} - {friend}")


# Use Enumerate Function to get Index from List with Start Index
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
for index, friend in enumerate(friends, start=1):
    print(f"{index} - {friend}")


# Get List of Tuples with Zip Function
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
print(list(zip([0, 1, 2, 3], friends)))


# Get List of Tuples with Enumerate Function
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
print(list(enumerate(friends)))


# Get a Dictionary with Enumerate Function
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
print(dict(enumerate(friends)))
