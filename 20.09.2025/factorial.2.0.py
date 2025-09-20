# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case: 0! and 1! are both 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call


while True:  # Loop to allow multiple entries
    user_input = input("Enter a number (or type 'q' to quit): ")

    # Check if the user wants to quit
    if user_input.lower() == 'q':
        print("Exiting program. Goodbye!")
        break

    # Convert input to integer
    num = int(user_input)

    # Check if the number is negative
    if num < 0:
        print("Factorial does not exist for negative numbers.")
    else:
        print(f"The factorial of {num} is {factorial(num)}")