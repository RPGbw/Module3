'''
Author: Brennan Whitng
date:06/26/2025
program: app that gets the users info about their car
'''

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def display_info(self):
        print("\nVehicle Information:")
        print(f"Vehicle Type: {self.vehicle_type}") 
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def get_vehicle_info():
    vehicle_type = "car"
    year = input("What is the year of your Vehicle: ")
    make = input("What is the make of your Vehicle: ")
    model = input("What is the model of your Vehicle: ")

    while True:
        doors = input("How many doors does your Vehicle have (2 or 4)?: ")
        if doors in ['2', '4']:
            break
        print("Please Enter 2 or 4 doors.")
    
    while True:
        roof = input("What kind of roof does your Vehicle have (solid or sunroof)?: ").lower()
        if roof in ['solid', 'sunroof']: 
            break
        print("Please enter either solid or sunroof.")

    return vehicle_type, year, make, model, doors, roof

if __name__ == "__main__":
    vehicle_data = get_vehicle_info()
    car = Automobile(*vehicle_data)
    car.display_info()
