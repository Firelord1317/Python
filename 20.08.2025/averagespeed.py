s1 = int(input("Enter your first speed: "))
s2 = int(input("Enter your second speed: "))
s3 = int(input("Enter your third speed: "))

average = (s1 + s2 + s3) / 3
print("Average is:", average)

if s1<average:
    print("First speed is below average with a difference of:", average - s1)
if s2<average:
    print("Second speed is below average with a difference of:", average - s2)
if s3<average:
    print("Third speed is below average with a difference of:", average - s3)