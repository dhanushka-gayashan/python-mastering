# Combind 2 Lists and create a Dictionary
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
time_since_seen = [3, 7, 15, 11]

long_timers = dict(zip(friends, time_since_seen))
print(long_timers)


# Combine Multipe Lists and create a List of Tuples
friends = ["Dhanushka", "Gayashan", "Chamari", "Nimalka"]
time_since_seen = [3, 7, 15, 11]

long_timers = list(zip(friends, time_since_seen, [1, 2, 3, 4]))
print(long_timers)
