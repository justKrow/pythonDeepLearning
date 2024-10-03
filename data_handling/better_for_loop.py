inventory_name = ['Screw', 'Wheel', 'Metal Parts',
                  'Rubber bits', 'Screrwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 32, 24]

for name, number in zip(inventory_name, inventory_numbers):
    print(f'{name} current inventory : {number}')

for index, thing in enumerate(inventory_name):
    print(f'{index} : {thing}')
    if index == len(inventory_name) // 2:
        print('Halfway through the inventory')

print(list(enumerate(zip(inventory_name, inventory_numbers))))

for index, (name, count) in enumerate(zip(inventory_name, inventory_numbers)):
    print(f'{name} [id: {index}] - inventory : {count}')
