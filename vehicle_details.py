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
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")
    
    def user_input():
        vehicle_type = input("Enter the type of vehicle: ").lower() 
        year = input("Enter the year of the vehicle: ")
        make = input("Enter the make of the vehicle: ").capitalize()
        model = input("Enter the model of the vehicle: ").capitalize()
        
        while True:
            doors = input("Enter the number of doors (2 or 4): ")
            if doors in ["2", "4"]:
                break
            else:
                print("Invalid input. Please enter 2 or 4.")

        while True:
            roof = input("Enter the type of roof (solid or sunroof): ").lower()
            if roof in ["solid", "sunroof"]:
                break
            else:
                print("Invalid input. Please enter 'solid' or 'sunroof'.")
        auto = Automobile(vehicle_type, year, make, model, doors, roof)
        return auto


if __name__ == "__main__":
    user_automobile = Automobile.user_input()
    user_automobile.display_info()