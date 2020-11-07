print(bytes([102, 111, 111]))

print(list(b'foo bar'))

print(tuple(b'foo bar'))

print(type("Some string"))

print(type(b"some bytes"))

print(bytearray(b'some types'))

nus = "Rick and Carl and Laurie"
#print(nus.encode(encoding, errors))

substrings = ["These ", "are ", "strings ", "to ", "concatenate."]
s = ""

for substring in substrings:
    s += substring

# using empty literals.
s = "".join(substrings)
print(s)

# using unbound method call
str.join("", substrings)

print(s)

s_a = ','.join(['some', 'comma', 'separated', 'values'])

print(s_a)


def conquer():
    from sys import version_info
    altty = "This is Python {}.{}".format(*version_info)
    #use_string_format = 'Some string with included % value' % 'other'
    #alt_string_format = 'Some string with included { other } value'.format(other='other')
    return altty

print(conquer())



