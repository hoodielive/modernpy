import json

with open('odu.json', 'r') as f:
    data = json.load(f)

first_odu = data['odus'][0]
second_odu = data['odus'][1]
third_odu = data['odus'][2]
fourth_odu = data['odus'][3]

print(first_odu)
print(first_odu['name'])
print(first_odu['meaning'])
print(first_odu['orientation'])
print(first_odu['element'])


userInput = input(str("What Odu do you want to know: "))

if userInput == first_odu['name'] or userInput == first_odu['orientation']:
    print(first_odu['meaning'])
