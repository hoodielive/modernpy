x = 10
y = 'hello, world'
items = [10, 20]

names = ['dave', 'Thomas', 'Lewis', 'paula']
names = names.sort(key=lambda name: name.upper())

print(names)

def greeting(name):
    print("hello", name)

greeting('Guido')

print(greeting)

g = greeting

g('Guide')

items.append(greeting)

print(items[2])

print(items[2]('Osa Meji'))

import time
def after(seconds, func):
    time.sleep(seconds)
    func()

def hello():
    print('Hello, Howdy')

after(5, hello)
