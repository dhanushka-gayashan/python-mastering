cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]


# Define Break
for status in cars:
    if status == "faulty":
        print("Stopping the production line!!")
        break

    print(f"This car is {status}")
    print("Shipping new car to customer!!")


# Define Continue
for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...!!")
        continue

    print(f"This car is {status}")
    print("Shipping new car to customer!!")