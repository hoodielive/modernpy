class Car:
    # construct (paramaterized constructor)
    def __init__(self):
        print("This is a non-paramaterized constructor!")

    def model(self, name):
        print("My first car was a: ", name)

corolla = Car() 
corolla.model("Toyota Corolla")