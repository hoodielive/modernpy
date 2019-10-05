class Car: 
    def start(self):
        print("Car started!")

    def reverse(self): 
        print("Car taking a reverse")

def main():
    volvo = Car()
    volvo.start() 
    volvo.reverse() 

if __name__ == "__main__":
    main()