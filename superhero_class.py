# Parent class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and my power is {self.power}!")

# Child class
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")


# Polymorphism in action
class Speedster(Superhero):
    def introduce(self):
        print(f"I’m {self.name}, the fastest from {self.origin} 🏃💨!")


# Creating objects and testing methods
hero1 = Superhero("Shadow Ninja", "Invisibility", "Japan")
hero2 = FlyingHero("Sky Blazer", "Wind Control", "Skytopia", 500)
hero3 = Speedster("FlashStrike", "Super Speed", "SpeedRealm")

hero1.introduce()
hero2.introduce()
hero2.fly()
hero3.introduce()  # Polymorphic method
