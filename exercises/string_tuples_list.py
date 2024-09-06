test_string = "this is a string"
test_list = [1, 2, 3, 4]

# string to list
print(list(test_string))
print(test_string.split())

# list to string
print(''.join(['one', 'two', 'three']))
print(str(test_list))

# indexing a string
print(test_string[0])
print(test_string[-1])

# exercise
# remove all the stuff to get only 1 2 3 4
print(str(test_list).strip('[').strip(']').replace(',', ''))
