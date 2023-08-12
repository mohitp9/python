class Vehicle:
    def __init__(self, registration_number, vehicle_type):
        self.registration_number = registration_number
        self.vehicle_type = vehicle_type

    def display_info(self):
        return f"Type: {self.vehicle_type}, Registration: {self.registration_number}"

class Car(Vehicle):
    def __init__(self, registration_number, brand, passengers):
        super().__init__(registration_number, "Car")
        self.brand = brand
        self.passengers = passengers

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Brand: {self.brand}, Passengers: {self.passengers}"

class Bus(Vehicle):
    def __init__(self, registration_number, route_number, capacity):
        super().__init__(registration_number, "Bus")
        self.route_number = route_number
        self.capacity = capacity

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Route: {self.route_number}, Capacity: {self.capacity}"

class EmergencyVehicle(Vehicle):
    def __init__(self, registration_number, vehicle_type, purpose):
        super().__init__(registration_number, vehicle_type)
        self.purpose = purpose

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Purpose: {self.purpose}"

class PoliceCar(EmergencyVehicle):
    def __init__(self, registration_number):
        super().__init__(registration_number, "Police Car", "Law Enforcement")

class Ambulance(EmergencyVehicle):
    def __init__(self, registration_number):
        super().__init__(registration_number, "Ambulance", "Medical Emergencies")

class TrafficControlTower:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle.display_info())
            print("=" * 30)

# Usage
if __name__ == "__main__":
    tower = TrafficControlTower()

    car1 = Car("ABC123", "Toyota", 4)
    car2 = Car("XYZ789", "Honda", 5)
    bus = Bus("DEF456", "Route 101", 30)
    police_car = PoliceCar("POL123")
    ambulance = Ambulance("AMB456")

    tower.add_vehicle(car1)
    tower.add_vehicle(car2)
    tower.add_vehicle(bus)
    tower.add_vehicle(police_car)
    tower.add_vehicle(ambulance)

    tower.display_all_vehicles()
