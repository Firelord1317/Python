
dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}


print("Test Dictionary:", dict)
value = int(input("Enter the value you want to check the frequency of: "))


frequency = list(dict.values()).count(value)


print("The frequency of value", value, "is:", frequency)
