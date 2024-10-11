class Monster:
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self, amount):
        print("Monster has attacked")
        print(f"{amount} of damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("Monster has moved")
        print(f"Speed: {speed}")


class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f"Fish swims with {self.speed} speed")


class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(health=health, energy=energy, speed=speed, has_scales=has_scales)


# mro - > method resolution order
# print(Shark.mro)

shark = Shark(bite_strength=50, health=200,
              energy=55, speed=120, has_scales=False)
print(shark.speed)
