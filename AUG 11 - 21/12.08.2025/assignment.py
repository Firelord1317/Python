friend1 = "4/5/2016"
friend2 = "2/3/2013"
friend3 = "3/5/2018"
friend4 = "3/4/2011"
friend5 = "6/10/2000"

print("Hello, whose birth date would you like to view")
friend = input("\nEnter the friend e.g friend1: ")

# I have used two equal sins because one assigns value to the variable and two are use to compare values
# I have used elif to check multiple conditions and else to handle the case when none of the conditions are met

if friend == "friend1":
    print("Birth date of selected person is:", friend1)
elif friend == "friend2":
    print("Birth date of selected person is:", friend2)
elif friend == "friend3":
    print("Birth date of selected person is:", friend3)
elif friend == "friend4":
    print("Birth date of selected person is:", friend4)
elif friend == "friend5":
    print("Birth date of selected person is:", friend5)
else:
    print("Friend not found.")

print("Thank you for using this program.")