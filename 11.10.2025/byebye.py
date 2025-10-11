valid =  False
while not valid:
    try:
        num = int(input("Enter an even number" 
        ": "))
        while num % 2 == 0:
            print("Bye")
            valid = True
    except ValueError:
        print("invalid input")
        