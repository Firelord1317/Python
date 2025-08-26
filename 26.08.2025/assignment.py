decimal = int(input("Enter a number: "))

binary = ""
num = decimal
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2


print("Binary representation of", decimal, "is: ", end="")
for digit in binary:     
    print(digit, end="")
