# You have to 5:30pm to complete the following Test.
# Start now. 

# Item 1
# Write a class that Models a Human. 
# The class should depict the head, shoulders (left and right), legs (left and right), reproductive organs (fe/male)
# As a mininum, there should be 3 methods that return body parts, sets body parts and returns a message about the class. Instantiate the class with the variable naming convention of lst_instantiation, 2nd and so forth - there should be 3 instantiations. 
class Human:
    def __init__(self, head, shoulders, legs, reproductive_organs):
        self._head = head
        self._shoulders = shoulders
        self._legs = legs
        self._repro_orgs = reproductive_organs
    def get_repro_orgs(self):
        return self._repro_orgs
    def get_head(self):
        return self._head
    def get_legs(self):
        return self._legs

lst_instantiation = Human('Medium head', 'Small Shoulders', 'Wide Legs and Hips', 'Vagina')

print(lst_instantiation)

print(lst_instantiation.get_legs())

# Item 2
# Write a base class with a few properties for a class that will inherit from it. 
class BaseClassy:
    def __init__(self, language, potential, salary):
        self._lang = language
        self._potent = potential
        self._salary = salary

# Item 3 What is duck typing? 
# Duck typing is ducking the specification of a type. 

# Write 4 try and except statements on Syntax Error, Value Error, Type Error, Attribute Error

# Write 5 functions depicting and returning *args and **kwargs 
def depictionOne(*args, **kwargs):
    return args and kwargs
def depictionTwo(*args, **kwargs):
    return args and kwargs
def depictionThree(*args, **kwargs):
    return args and kwargs
def depictionFour(*args, **kwargs):
    return args and kwargs
def depictionFive(*args, **kwargs):
    return args and kwargs


# Write 2 functions that returns and integer to another function.
def returnInt(dev):
    return dev
def returnInt2(dev):
    return dev

# Write 2 functions that have default arguments.
def funcDef(race=None):
    return race

def funcDef2(race=4):
    return race

# Write 3 lambda functions. 
lambda x: x * x
lambda a: a - a
lambda p: p / p

# Use the filter function to filter from a list that contains the integer 5 (should be excluded)
def filFunc(app):
    stringy = ['string', 'index', 'integer', 'float', 'array']
    if app in stringy:
        return True
    else:
        return False

seq = ['stratum', 'stratos', 'string', 'array']

filter_that_mug = filter(filFunc, seq)

print('The filtered items are: ')

for s in filter_that_mug:
    print(s)

# What is a Stack? 

# What is a queue? 

# Write 3 list comprehensions. 
a_list_to_play_with = [1, 2, 3, 4, 5]
listcomp01 = [lister for lister in a_list_to_play_with]
listcomp02 = [lister for lister in a_list_to_play_with]
listcomp03 = [lister for lister in a_list_to_play_with]
print(listcomp01, listcomp02, listcomp03)

# Write 3 for-loops over a list. 
newlist = [1, 2, 3]
for items in newlist:
    print(items)
newerlist = [x for x in newlist]
print(newerlist)

# Write 3 for-loops over a dictionary. 
period = { 'ori': 'first_god', 'ada': 'programming language', 'nim': 'new heavy weight' }

for k, v in period.items():
    print("The key is: ", k, "and the value is: ", v)
for k, v in period.items():
    print("The key is: ", k, "and the value is: ", v)
for k, v in period.items():
    print("The key is: ", k, "and the value is: ", v)

# Write 3 for-loops over a Tuple.
tup = (1, 2, 3)

for t1 in tup:
    print(t1)

for t2 in tup:
    print(t2)

for t3 in tup:
    print(t3)

# Write a for-loop over a string. 
newstring = 'string'
for elem in newstring:
    print(elem)

# What is the difference between an Array and a List? 
print('Nothing.')

# Write 3 dictionary comprehensions. 
dict01 = { 'firstname': 'Law', 'lastname': 'abstract' }
dictcomp01 = {k:v for (k,v) in dict01.items()}
dictcomp02 = {k:v for (k,v) in dict01.items()}
dictcomp03 = {k:v for (k,v) in dict01.items()}
print(dictcomp01)
print(dictcomp02)
print(dictcomp03)

# Unpack 2 tuples.
a = (1, 2)
a, b = a
print(a, b)

b = (3, 4)
c, d = b
print(c, d)

# What does the dir function do? 
print("It returns a list of attributes.")

# Explain the Module search path. 
# yawn.




