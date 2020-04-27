# Define a List
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
print(friends)


# Access Elements
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])


# Get Length
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
print(len(friends))


# Inner List
friends = [
    ["Dhanushka", 33], 
    ["Gayashan", 32], 
    ["Chamari", 31], 
    ["Nimalka", 30]
]

print(friends[0][0])
print(friends[0][1])

print(friends[1][0])
print(friends[1][1])

print(friends[2][0])
print(friends[2][1])

print(friends[3][0])
print(friends[3][1])


# Append
friends = ["Dhanushka", "Gayashan", "Chamari"]
friends.append("Nimalka")
print(len(friends))


# Append Inner List
friends = [
    ["Dhanushka", 33],
    ["Gayashan", 32],
    ["Chamari", 31]
]
friends.append(["Nimalka", 30])


# Remove
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
friends.remove("Nimalka")
print(len(friends))


# Remove Inner List
friends = [
    ["Dhanushka", 33],
    ["Gayashan", 32],
    ["Chamari", 31],
    ["Nimalka", 30]
]
friends.remove(["Nimalka", 30])
