# Select Elements  
ages = [22, 35, 27, 21, 20]

odds = [age for age in ages if age % 2 == 1]
print(odds)


# Select Friends from Guests with "List Comprehension"
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
guests = ["Jack", "dhanushka", "Jil", "chamari"]

present_friends = [
    guest.title() 
    for guest in guests 
    if guest.lower() in [friend.lower() for friend in friends]
]

print(present_friends)
