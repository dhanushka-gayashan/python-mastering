# Define 
currencies = 0.8, 1.2
usd, eur = currencies
print(usd)
print(eur)


# Work with List of Tuples
friends = [("Dhanushka", 33), ("Gayashan", 32), ("Chamari", 31), ("Nimalka", 30), ]

for friend in friends:
  name, age = friend
  print(f"{name} is {age} years old.")

for name, age in friends:
  print(f"{name} is {age} years old.")


