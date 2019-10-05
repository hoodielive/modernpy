class Car: 
    car_type = "suv"
    model = "S90"
    mileage = 6

    def start(self):
        print("Car started!")

    def reverse(self): 
        print("Car taking a reverse")


new_car = Car() 
print(new_car.car_type)
print(new_car.model)
print(new_car.mileage)