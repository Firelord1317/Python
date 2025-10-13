# Age Counter Program
# Checks if the entered age is correct and whether it is even or odd

try:
    # Ask user for age
    age = int(input("Enter your age: "))

    # Check if the age is valid
    if age < 0 or age > 120:
        print("Error: Please enter a realistic age between 0 and 120.")
    else:
        print(f"Your age is {age}.")

        # Check if even or odd
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")

except ValueError:
    print("Error: Invalid input! Please enter a number only.")
