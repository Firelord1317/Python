base = int(input("Enter number: "))
power = int(input("Enter power: "))

result = 1
for i in range(power):
    result *= base

print("Answer:", result)
