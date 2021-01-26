import sys

s = u'Caf\xe9'  # Café

print(s)

print([_c for _c in s])

print(type(s))

print(len(s))

bs = bytes(s, encoding='utf-8')

print(bs)

print(len(bs))

for _c in s: print('U+%04x' % ord(_c))

print(sys.getsizeof(bs))
print(sys.getsizeof(s))