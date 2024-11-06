class Vehicle:
    def get_sound(self):
        print("vehicle's brum brum")

    def get_owner(self) -> str: #już dodałem metode i działa
        return "Unknown owner"
class Car(Vehicle):
    def __init__(self, owner: str, table: str):
        self.owner = owner
        self.table = table

    def get_sound(self):
        print("car's brum brum")

    def get_owner(self) -> str:
        return self.owner

# Tworzenie instancji klas
vehicle_instance = Vehicle()
car_instance = Car(owner="Paweł", table="XYZ 1234")

# Wywołanie metody get_sound
vehicle_instance.get_sound()  # Powinno wypisać "vehicle's brum brum"
car_instance.get_sound()      # Powinno wypisać "car's brum brum"

# Wywołanie metody get_owner
try:
    print(car_instance.get_owner())  # Powinno wypisać właściciela ("Paweł")
    print(vehicle_instance.get_owner())  # To spowoduje błąd, bo Vehicle nie ma metody get_owner(juz ma bo dodałem)
except AttributeError as e:
    print(f"Błąd: {e}")
