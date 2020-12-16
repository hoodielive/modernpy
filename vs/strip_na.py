import time
from functools import partial

friends = ['Ifagbemi', 'OsaTunga', 'Fatuga', 'Sogo']

def after(seconds, func):
   time.sleep(seconds)
   return func

def greeting(entry):
    wisdom = [partial(entry) for entry in friends]
    return wisdom

greeting(friends)
#print(after(10, greeting(friends)))

