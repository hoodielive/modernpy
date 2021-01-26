# Polymorphism is method overloading and method overriding 
# Its also operator overloading 

class Man: 
    def sayHi(self, name=None):
        if name is not None: 
            print("Hi " + name)
        else:
            print("Hi!")
        
obj = Man() 
obj.sayHi("Larry")

