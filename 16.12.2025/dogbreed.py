class Dog:
    # class variable
    species = "Dog"

    # constructor with two instance variables
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    # method to display details
    def display_details(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age, "years")
        print()


# creating objects of two different breeds
dog1 = Dog("German Shepherd", 3)
dog2 = Dog("Labrador", 5)

# displaying details
dog1.display_details()
dog2.display_details()
