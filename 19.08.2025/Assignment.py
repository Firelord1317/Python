char = input("Enter a letter: ")

if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
    ascii_val = ord(char)     
    masked = ascii_val & 127

    print(f"ASCII of '{char}' = {ascii_val}")

    
    if ascii_val is masked:
     print("Identity check passed.")
else:
    print("Identity check failed.")
