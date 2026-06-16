#simple inheritance

# Base class

class Animal:
    def __init__(self, name):
        self.name =  name

    def speak(self):
        print(f"{self.name} make this sound")

# dervied class
class Dog(Animal):
    def speak1(self):
        print(f"{self.name} barks")



animal = Animal("Horse")
animal.speak()

dog = Dog("dog")
dog.speak()