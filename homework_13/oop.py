class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self, increase):
        self.max_speed += increase

    def break_speed(self, decrement):
        self.max_speed -= decrement
        if self.max_speed < 0:
            self.max_speed = 0

    def mileage_info(self):
        print(f"Mileage: {self.mileage}")


class Animal:
    def __init__(self, firstname, lastname, weight, eyes):
        self.firstname = firstname
        self.lastname = lastname
        self.weight = weight
        self.eyes = eyes

    def jump(self, weight_jump):
        return f"{self.firstname} jumps to a height of {weight_jump}"

    def eat(self, food):
        return f"{self.firstname} eat {food}"

    def breath(self, breath):
        return f"{self.firstname} make {breath} breath in minuet"


Toyota = Vehicle(220, 10_000)
Toyota.increase_speed(30)
print(Toyota.max_speed)

Toyota.break_speed(100)
print(Toyota.max_speed)

Toyota.mileage_info()
# ------------------------------------------------

Audi = Vehicle(290, 142_472)
Audi.increase_speed(32)
print(Audi.max_speed)

Audi.break_speed(230)
print(Audi.max_speed)

Audi.mileage_info()

# __________________________________________________

animal_1 = Animal("Max", "Fox", 10, 2)

print(animal_1.jump(5))
print(animal_1.eat("meat"))
print(animal_1.breath(30))
# ------------------------------------------------

animal_2 = Animal("Buddy", "Dog", 15, 2)

print(animal_2.jump(3))
print(animal_2.eat("bones"))
print(animal_2.breath(24))
