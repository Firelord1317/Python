print("Select the type of ride:")
print("1. Car")
print("2. Bike")

choice = int(input("Enter your choice (1 or 2): "))

if (choice == 2):
    print("You have selected a Bike ride.")
    print("What type of bike?")
    print("1. Scooty\n")
    print("2. Scooter\n")

    choice2 = int(input("Enter your choice (1 or 2): "))
    if (choice2 == 1):
        print("You have selected a Scooty.")
    else:
        print("You have selected a Scooter.")

elif (choice == 1):
    print("You have selected a Car ride.")
    print("What type of car?")
    print("1. Sedan\n")
    print("2. XUV\n")

    choice3 = int(input("Enter your choice (1 or 2): "))
    if (choice3 == 1):
        print("You have selected a Sedan.")
    else:
        print("You have selected an XUV.")
else:
    print("Invalid choice!")