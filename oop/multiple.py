class Animal:
    def eat(self):
        print("Eating..")

class Dog(Animal):
    def bark(self):
        print("Barking..")

class Puppy(Dog): 
    def weep(self):
        print("Weeping..")

d = Puppy()
d.bark() 
d.weep()
d.eat()