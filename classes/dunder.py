class Monster:

    # attributes
    # health = 90
    # energy = 40

    # methods
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        print("Monster spawned")

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __call__(self):
        print("Monster was called")

    def __add__(self, other):
        return self.health + other

    def __str__(self):
        return "MONSTERRRRR"

    def attack(self, amount):
        print(f"Monster attacks for {amount} damage! ")
        self.energy -= 20
        print(f"Monster has {self.energy} remaining energy")

    def move(self, speed):
        print(f"Monster moves at {speed} speed")


monster1 = Monster(75, 90)
print(len(monster1))
print(abs(monster1))
print(monster1.__dict__)
print(vars(monster1))
monster1()
print(monster1 + 10)
print(str(monster1))
print(monster1)
