print("Enter marks obtained in 4 subjects")
math = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))
hindi = int(input("hindi: "))

sum = math + english + science + hindi
print("The total marks obtained is:", sum)

perc = (sum / 400) * 100

print( end="percentage mark =")
print(perc)
