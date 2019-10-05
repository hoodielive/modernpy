class Family: 
    name=""

    def __init__(self, name):
        self.name = name 

    def printName(self):
        print("name = " + self.name) 

class Relative(Family):
    def __init__(self, name): 
        self.name = name 

    def doPython(self):
        print("Pro in Python!")


vince = Family("vince")
vince.printName()

brandon = Relative("Brandon")
brandon.printName()
brandon.doPython()