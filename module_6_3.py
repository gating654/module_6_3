class Vehicle:
    def __init__(self, vehicle_type="none"):
        self.vehicle_type = vehicle_type


class Car(Vehicle):
    def __init__(self, vehicle_type, price=1000000):
        super().__init__(vehicle_type)
        self.price = price

    def horse_powers(self):
        print("Кол-во лошадиных сил.")


class Nissan(Car, Vehicle):
    def __init__(self, price, vehicle_type):
        super().__init__(price, vehicle_type)
        super().horse_powers()


n = Nissan(2500000, "none")
print(n.vehicle_type, n.price)
