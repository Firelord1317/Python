import random

class FruitQuiz:

# Create a constructor
    def __init__(self):

# Create a dictionary of fruits as keys and color as

        self.fruits={'apple':'red',
        'orange' : 'orange',
        'watermelon':'green',
        'banana': 'yellow',
        'Grapes': 'purple',
        'kiwi': 'brown'}
        

# Function for the quiz, here a fruit will be chosen randomly
def quiz(self):
    while (True):

        fruit, color = random.choice(list(self.fruits.items()))

        print("What is the color of {}?".format(fruit))
        value = input()

        if(value.lower() == color):
            print("Correct answer")
        else:
            print("Wrong answer")

        option = int(input("Enter 0 if you want to play again otherwise 1 : "))
        if(option):
            break
print("welcome to fruit quiz ")
fq = FruitQuiz()
fq.quiz()