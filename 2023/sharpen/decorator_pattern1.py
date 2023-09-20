from datetime import datetime

def my(func):
    def wrapper():
        print("Before function is called.")
        func()
        print("After function is called.")

def say_whee():
    print('Whee!')

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass # Hush
    return wrapper

print(type(say_whee)) # type Function here.
print(say_whee)
#say_whee = my(say_whee) # type None here? why?
print(type(not_during_the_night))
print(not_during_the_night(say_whee)())

larson = my(say_whee)
print(type(larson))
print(larson)
