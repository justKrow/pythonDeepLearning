my_list = []
for num in range(0, 100):
    my_list.append(num)

print(my_list)

# my_list_comp = [(num, num * 2, num) for num in range(0, 100) if num < 20 else 0] #else does not work

my_list_comp = [(num, num * 2, num) if num <
                20 else 0 for num in range(0, 100)]
print(my_list_comp)

inventory_name = ['Screw', 'Wheel', 'Metal Parts',
                  'Rubber bits', 'Screrwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 32, 24]

replenish_list = [(name, stock) for name, stock in zip(
    inventory_name, inventory_numbers) if stock < 25]

print(replenish_list)

# combine list comprehension
combined_comp = [[(x, y) for x in range(5)] for y in range(10)]
for row in combined_comp:
    print(row)

chess_board = [[(letter, num) for num in range(1, 9)]
               for letter in 'ABCDEFGH'[::-1]]
for row in chess_board:
    print(row)

set_comp = {num for num in range(100)}
dict_comp = {num: num for num in range(100)}
tuple_comp = tuple(num for num in range(100))

dict_comp = {letter: [1, 2, 3, 4, 5] for letter in 'ABCDE'}
print(dict_comp)
