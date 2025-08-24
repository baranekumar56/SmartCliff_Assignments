

class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return "Brand :" + self.brand + "\nYear :" + self.year + "\n"

class Car(Vehicle):

    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def display_car_info(self):
        return super().display_info() + "Model :" + self.model


c = Car("Toyota", "2002", "xyz")
print(c.display_car_info())

