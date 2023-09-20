def say_hello(name):
    return f'Hello {name}'

def be_awesome(name):
    return f'Yo {name}, together we are the awesomest!'

my_list = [say_hello, be_awesome]

print(my_list[0]('Lawrence'))
print(my_list[1]('Lawrence'))


def greet_Oyeku(greeter_func):
    return greeter_func("Oyeku")

print(greet_Oyeku(say_hello))
print(greet_Oyeku(be_awesome))
