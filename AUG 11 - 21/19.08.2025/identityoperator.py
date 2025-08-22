x = 5
if type(x) is int:
    print("True")
else:
    print("False")

  
x = 5.0
if type(x) is not float:
    print("True")
else:
    print("False")


x = 20
y = 20
if x is y:
    print("X and Y have the same identity")
else:
    print("X and Y have different identities")
