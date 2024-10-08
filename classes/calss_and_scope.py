# scope problem
def update_health(amount):
    monster.health += amount


# health = 10
# print(health)
# update_health(5)
# print(health)

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.set_energy(energy)

    def update_energy(self, amount):
        self.energy += amount

    def set_energy(self, energy):
        new_energy = energy * 2
        self.energy = new_energy

    # the monster class should have a method that lowers the health -> get_damage(amount)
    def get_damage(self, amount):
        self.health -= amount


monster = Monster(health=100, energy=50)
update_health(50)
monster.update_energy(30)
print(monster.health)
print(monster.energy)

# exercise
# create a hero class with 2 parameters: damage, monster
# the monster class should have a method that lowers the health -> get_damage(amount)
# the hero class should have an attack method that calls the get_damage method from the monster
# the amount of damage is hero.damage


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)


hero = Hero(damage=40, monster=monster)
hero.attack()
print(monster.health)
