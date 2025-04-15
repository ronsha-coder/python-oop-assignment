# Parent class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def specs(self):
        print(f"{self.brand} {self.model} has {self.storage}GB of storage.")

# Child class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def specs(self):
        print(f"{self.brand} {self.model} with {self.storage}GB and {self.cooling_system} cooling system is perfect for gaming!")


# Polymorphism example
class FoldablePhone(Smartphone):
    def specs(self):
        print(f"{self.brand} {self.model} is a sleek foldable device with {self.storage}GB of storage!")


# Testing objects
phone1 = Smartphone("iPhone", "15 Pro", 256)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "LiquidX")
phone3 = FoldablePhone("Samsung", "Galaxy Z Fold 5", 512)

phone1.specs()
phone2.specs()
phone3.specs()
