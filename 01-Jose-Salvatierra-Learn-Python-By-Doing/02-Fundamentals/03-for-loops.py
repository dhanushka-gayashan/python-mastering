# Iterate pre-defined number of times
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements:
    print("Hello World")

for _ in elements:
    print("Hello World")


# Use range(end)
for index in range(10):
    print(index)

for _ in range(10):
    print("Hello World")


# Use range(start, end)
for index in range(5, 10):
    print(index)


# Use range(start, end, step)
for index in range(2, 20, 3):
    print(index)
