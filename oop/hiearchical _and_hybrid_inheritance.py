class Parents:
    def gen(self):
        x = 1
        print(x)

class Child1(Parents):
    pass 

class Child2(Parents):
    pass 

issubclass(Child1, Parents) and issubclass(Child2, Parents)

child = Child1() 
child.gen()

child = Child2() 
child.gen()