char = input("Enter a character: ")

if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print("You entered a letter.")
elif (char >= '0' and char <= '9'):
    print("You entered a number.")
elif not ( (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9') ):
    print("You entered a special character.")

