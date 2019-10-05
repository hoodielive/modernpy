# destructors delete/erase the existence of a created object 
# garbage collection frees memory associated with an object 
# destructors also deal with deleting resources other than memory and performs final cleanup
# a Class can implement the special method __del__() = destructor that is invoked when the instance is destroyed

class Car:
    def __init__(self):
        print("Car created!")

    def __del__(self):
        print("Destructor is called and Car is now deleted.")
        

lexus = Car() 
del lexus