class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print("Monster has attacked")
        print(f"{amount} of damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("Monster has moved")
        print(f"Speed: {speed}")


class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Monster.__init__(self, health, energy)
        super().__init__(health, energy)
        self.speed = speed
        super().move(10)

    def bite(self):
        print("Shark has bitten")

    def move(self):
        print("Shark has moved")
        print(f"Speed: {self.speed}")


shark = Shark(speed=113, health=120, energy=75)
shark.attack(20)
shark.bite()
shark.move()

# exercise
# create scorpion class that inherits from monster
# health and energy from the parent
# poison damage attribute
# overwrite the damage method to show poison damage


class Scorpion(Monster):
    def __init__(self, scorpion_health, scorpion_energy, poison):
        super().__init__(health=scorpion_health, energy=scorpion_energy)
        self.poison = poison

    def attack(self):
        print("Scorpion has attacked")
        print(f"{self.poison} of poison damage was dealt")
        self.energy -= 35


scorpion = Scorpion(scorpion_health=75, scorpion_energy=120, poison=50)
scorpion.attack()
print(scorpion.health)
