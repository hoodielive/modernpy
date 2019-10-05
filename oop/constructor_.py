class Car:
    # construct (paramaterized constructor)
    def __init__(self, name):
        print("This is a non-paramaterized constructor!")
        self.name = name

    def model(self):
        print("My first car was a: " + self.name)

corolla = Car("Toyota Corolla") 
corolla.model()