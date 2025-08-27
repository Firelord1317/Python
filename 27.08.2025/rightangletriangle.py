print("Half pyramid pattern of stars('*'):")
n = int(input("Enter the number of rows: "))
for i in range(n):
    print("* " * i)
    for j in range(i+1):
        print("*", end=" ")
    print()