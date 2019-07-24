random_bits = 0 

for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i 

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry'] 

# iterate over a list and know the index of current item in list 
for i in range(len(flavor_list)):
    flavor = flavor_list[i] 
    print('%d: %s' % (i + 1, flavor)) 
