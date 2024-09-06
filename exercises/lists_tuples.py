# list
my_list = [1, 2, 3, 4.5, 'word']
print(len(my_list))
my_list.append(10)
print(my_list)


# tuple
my_tuple = (1, 2, 3, 4.5, 'word', [7, 8, 9])
print(my_tuple)
# my_tuple.append(43)

# how to pick elements from a list or tuple
my_list[3] = 5
print(my_list)
print(my_tuple[4])
print(my_tuple[5][2])

# exercise
# get the word / string 'hello :)'
exercise_list = ['first entry', [123, 456, [0, 'hello :)']], 'bye']
print(exercise_list[1][2][1])
