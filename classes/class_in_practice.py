class Monster:

    # attributes
    health = 90
    energy = 40

    # methods
    def attack(self, amount):
        print(f"Monster attacks for {amount} damage! ")
        self.energy -= 20
        print(f"Monster has {self.energy} remaining energy")

    def move(self, speed):
        print(f"Monster moves at {speed} speed")


monster = Monster()
print(monster.health)
monster.attack(50)
monster.move(50)
