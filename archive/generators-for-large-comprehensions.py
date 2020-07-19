value = [ len(x) for x in open('/tmp/my_file.txt') ] 
print(value) 
roots = ((x, x**0.5) for x in value) 

print(next(roots)) 
