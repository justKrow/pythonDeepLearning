# basics
test_dict = {'A': 1, 'B': 'it is a B', 1: True}
print(test_dict)
print(test_dict.items())
print(len(test_dict))

# converting dict
print(list(test_dict))
print(tuple(test_dict))
print(str(test_dict))

# indexing
print(test_dict['A'])
print(test_dict.get('Z'))  # does not crash if no key foun

# update method
new_data = {'C': 'it is a C no joke'}
test_dict.update(new_data)
print(test_dict)
