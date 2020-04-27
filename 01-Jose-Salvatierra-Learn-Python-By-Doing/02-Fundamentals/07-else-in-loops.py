# Without ELSE Keyword
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

all_successful = True

for status in cars:
    if status == "faulty":
        print("Stopping the production line!!")
        all_successful = False
        break

    print(f"This car is {status}")
    print("Shipping new car to customer!!")

if all_successful:
    print("ALl cars build successfully. No faulty cars!!")


# With ELSE Keyword : Only run if for-loop iterate over all elements in the List
cars = ["ok", "ok", "ok", "ok", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!!")
        break

    print(f"This car is {status}")
    print("Shipping new car to customer!!")
else:
    print("ALl cars build successfully. No faulty cars!!")
