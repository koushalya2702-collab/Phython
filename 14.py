# Classes and Objects

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"Car Brand:{self.brand},Model:{self.model}")

my_car=Car("Toyota","Corolla")
my_car.display_info()


# Attributes (Instance Variables) and Methods
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello,my name is {self.name} and i am {self.age} years old")

person1=Person("Arjun",30)
person2=Person("Megha",56)

person1.greet()
person2.greet()


# Creating Multiple Objects from a Class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating multiple objects
dog1 = Dog("Rex", "Golden Retriever")
dog2 = Dog("Bolt", "Beagle")

dog1.bark()
dog2.bark()