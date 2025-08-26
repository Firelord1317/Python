string = input("Enter your word: ")
char = input("Enter the character to be searched: ")
i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1
print("The character: ", char, " occurred ", count, " times.")