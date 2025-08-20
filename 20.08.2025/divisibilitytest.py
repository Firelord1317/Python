print("Enter a number (Numerator):")
mumn = int(input())
print("Enter a number (Denominator):")
numd = int(input()) 

if mumn % numd == 0:
    print("\n" + str(mumn) + " is divisible by " + str(numd))
else:
    print("\n" + str(mumn) + " is not divisible by " + str(numd))   