car1_price = 5000

# created objects are assigned to heap 
# reference objects are assigned to stack 

car2_price = car1_price 
if (id(car1_price) == id(car2_price)):
    print("Car 1 and Car 2 have the same object value & MemoryID = ", hex(id(car1_price)))

car1_price = car1_price + 10
if (id(car1_price) != id(car2_price)):
    print("Car 1 and Car 2 have a different object value & MemoryID = ", hex(id(car1_price)), hex(id(car2_price)))

car3_price = 5000 
if (id(car2_price) == id(car3_price)):
    print("Car2 and Car3 have the same memory value & id = ", hex(id(car3_price)))
else: 
    print("Car2 and Car3 have different object values and id = ", hex(id(car3_price)), hex(id(car2_price)))

car1_price = None 
print("Value is None.")
print("Garbage collector emptied to memory.. lol")







