list1 = [4, 2, 3, 4, 5]
print(sorted(list1, reverse=True))

list2 = [('a', 3), ('b', 10), ('c', 5), ('d', 4)]


def sort_function(item):
    return item[1]


print(sorted(list2, key=sort_function))
print(sorted(list2, key=lambda item: item[1]))

inventory_name = ['Screw', 'Wheel', 'Metal Parts',
                  'Rubber bits', 'Screrwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 32, 24]
combined_list = list(zip(inventory_name, inventory_numbers))
print(combined_list)

print(sorted(combined_list, key=lambda item: item[1]))
print(sorted(combined_list, key=lambda item: len(item[0])))

my_list = [1, 2, 3, 4, 5]
# map - change values with a function inside of a iterable
print(list(map(lambda num: num**2, my_list)))
print([num ** 2 for num in my_list])

# filter - filter out values from a condition
print(list(filter(lambda num: num < 4, my_list)))
print([num for num in my_list if num < 4])
