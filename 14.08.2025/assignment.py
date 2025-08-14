print("Welcome to Arnav.org's official branch Autoroot!")
print("\nHere at Autoroot, we specialize in providing top-notch automation solutions to math problems like calculating averages, percentages, and more.")
choice = (input("\nPlease select option one(1) to try our square root finder for free: "))

choice = int(choice)

if choice == 1:
    num = int(input("\nEnter a number to find its square root: "))
    print("\nThe square root of the number is:", num**0.5)

else:
    print("\nInvalid choice. Please try again.")
    choice = int(input("\nPlease select option one(1) to try our square root finder for free: "))       

