a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

print("\nBefore swapping:")
print("a =", a, " b =", b, " c =", c)

a, b, c = c, a, b

print("\nAfter swapping:")
print("a =", a, " b =", b, " c =", c)
