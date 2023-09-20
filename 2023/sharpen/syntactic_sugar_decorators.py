def my(func):
    def wrapper():
        print("Before.")
        func() 
        print("After.")
    return wrapper

@my
def say_whee():
    print("Wheeeee!")

print(say_whee())
