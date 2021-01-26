def func(**kwargs):
""" This is to do something strange."""
    return kwargs

print(func(key="value"))
print(type(func(key="value")))

dictionary_01 = dict(key='value')
print(dictionary_01)
print(type(dictionary_01))
