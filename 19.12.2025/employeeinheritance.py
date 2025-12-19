# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person( object ):

#_init_ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        self.salary =  20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.post = "Kibera Intern"
    def display(self):
        print("Name :", self.name)
        print("ID Number :", self.idnumber)
        print("Salary :", self.salary)    
        print("Post :", self.post)


# child class
class Employee(Person):

    #_init_ is known as the constructor
    def __init__(self, name, idnumber, salary, post):
        # initialize parent attributes
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post

    def display(self):
        # reuse parent display to print all details
        super().display()

#creating an object of child class
a = Employee("Onyango", 886012, 20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, "Intern")        
# calling a function of the class Person using its instance
a.display()