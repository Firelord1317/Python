from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def speed(self):
        pass

# BMW class
class BMW(Vehicle):

    def start(self):
        print("BMW starts with a push button")

    def speed(self):
        print("BMW has a top speed of 250 km/h")

# Ferrari class
class Ferrari(Vehicle):

    def start(self):
        print("Ferrari starts with a roar")

    def speed(self):
        print("Ferrari has a top speed of 340 km/h")

# Polymorphism in action
vehicles = [BMW(), Ferrari()]

for v in vehicles:
    v.start()
    v.speed()
