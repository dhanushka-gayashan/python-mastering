# Define 
friends = {"Dhanushka", "Gayashan"}
print(friends)


# Empty Set
friends = set()
print(friends)


# Append - Do not add Dupliates
art_friends = {"Dhanushka", "Gayashan"}

art_friends.add("Chamari")
print(art_friends)

art_friends.add("Chamari")
print(art_friends)


# Compare Sets
art_friends = {"Dhanushka", "Gayashan", "Chamari"}
science_friends = {"Chamari", "Nimalka"}

only_arts = art_friends.difference(science_friends)
print(only_arts)

only_science = science_friends.difference(art_friends)
print(only_science)

only_one = art_friends.symmetric_difference(science_friends)
print(only_one) 

in_both = art_friends.intersection(science_friends)
print(in_both)

any_one = art_friends.union(science_friends)
print(any_one)
