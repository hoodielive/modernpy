class Parents:
    def gen(self):
        x = 1
        print(x)

class Father(Parents):
    pass

class Mother(Parents):
    pass 

class Child(Father, Mother):
    pass 

child_obj = Child() 

child_obj.gen()

