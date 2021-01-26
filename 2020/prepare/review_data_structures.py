# Lists.

todo = [ "pick up here", "buy groceries", "pay bills" ]

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

result = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]

for printed_result in X, Y, result: 
    print(X, Y, result)

for i in todo:
    print(i)

# Dictionaries.

User = { 
    "name" : "Jeriah", 
    "age": 27, 
    "email" : "someemail@email.com"
}

# Loop over Dictionary.
for i in User.items():
    print(i)

tuples = ("i", "am", "a", "tuple", "of", "strings")

for i in tuples:
    print(i)
