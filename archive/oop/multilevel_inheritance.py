
class Father(object):
    def __init__(self):
        super(Father, self).__init__()
        print("Father")

class Mother(object):
    def __init__(self):
        super(Mother, self).__init__()
        print("Mother")

class Son(Mother, Father): 
    def __init__(self):
        super(Son, self).__init__()
        print("Son")

Son()
