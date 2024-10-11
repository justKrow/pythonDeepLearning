class Monster:
    '''monster and its attributes'''

    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)
        self._id = 5

    def attack(self, amount):
        print("Monster has attacked")
        print(f"{amount} of damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("Monster has moved")
        print(f"Speed: {speed}")


monster = Monster(20, 10)

# private attributes
print(monster._id)

# hasattr and setattr
print(hasattr(monster, 'health'))
if hasattr(monster, 'energy'):
    print(f'Monster still has {monster.energy} energy')

monster.weapon = 'chainsaw'
print(monster.weapon)
setattr(monster, 'weapon', 'gun')
print(monster.weapon)

new_attributes = (['weapon', 'axe'], ['armor', 'leather'], ['potion', 'mana'])
for attr, value in new_attributes:
    setattr(monster, attr, value)
print(vars(monster))

# doc
print(monster.__doc__)
help(monster)
