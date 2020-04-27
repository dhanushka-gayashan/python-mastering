# Select Friends from Guests with "Set and Comprehension"
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
guests = ["Jack", "dhanushka", "Jil", "chamari"]

friends_lower = set([friend.lower() for friend in friends])
guests_lower = set([guest.lower() for guest in guests])

present_friends = guests_lower.intersection(friends_lower)
present_friends = {friend.title() for friend in present_friends}

print(present_friends)


# Select Friends from Guests with "Set and Comprehension"
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
guests = ["Jack", "dhanushka", "Jil", "chamari"]

friends_lower = {friend.lower() for friend in friends}
guests_lower = {guest.lower() for guest in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {friend.title() for friend in present_friends}

print(present_friends)
