print("Welcome to string operations in python!")
word = input("\nEnter a word to convert from uppercase to lowercase or lowercase to uppercase: ")

if word.isupper():
    print(word.lower())
          
else:
    print(word.upper())