# Dictionaries 

dictionary_a = {
    'firstname': 'Vincent',
    'lastname': 'Spivey',
    'age': 'unknown',
    'location': 'restricted'
}

def determineStuff():
    for k, v in dictionary_a.items():
        if k == 'firstname':
            print('Hello, my name is: ' + v)
        if k == 'lastname':
            print('And my lastname is: ' + v)
        if k == 'age':
            print('But I rather not reveal my age, so we will say it is: ' + v)
        if k == 'location':
            print('There whereabouts of my location is: ' + v)

determineStuff()
# set
set_a = { 3, 3, 3, 4, 4, 4 }
print(set_a)


