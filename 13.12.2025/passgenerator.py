import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/`~ "

length = int(input("Enter password length: "))

password = ""
for i in range(length):
    password += random.choice(letters)

print("Password:", password)