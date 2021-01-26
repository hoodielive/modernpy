# Python actually shows you the list of modules imported via:
# sys.modules - a dictionary that takes the module name and
# the value as the module object.

import sys

print(sys.path)
print(sys.modules['os'])
print(sys.builtin_module_names)