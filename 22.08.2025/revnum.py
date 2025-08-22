n = int(input("Enter a number: "))

print("Numbers from {0} to 1 are:".format(n))
for i in range(n, 0, -1):
    print(i, end=" ")