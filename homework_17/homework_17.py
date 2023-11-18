# 1
class Animal:
    def __init__(self, speed, top_jump):
        self.speed = speed
        self.top_jump = top_jump


# 2
class Cat(Animal):
    def cat_eat(self):
        pass

    def cat_sleep(self):
        pass


# 3
print(issubclass(Cat, Animal))
# True значить клас Cat успадковується від класа Animal


# 4
class Dog(Animal):
    def dog_barks(self):
        pass

    def dog_sleep(self):
        pass


# 5
print(Dog.__bases__)


# 6
class Mouse(Dog, Cat):
    def mouse_hiding(self):
        pass
