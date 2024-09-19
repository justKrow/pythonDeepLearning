test_set = {1, "this", "that", True, 1}  # eliminate the duplicates

# method
test_set.add(False)

print(test_set)
print(len(test_set))

# cant index or slice
# test_set[0]

test_set.pop()
print(test_set)

# type conversion for indexing
print(list(test_set)[2])

# comparison operators
sec1 = {1, 2, 3, 4, 5, 6, 6}
sec2 = {5, 6, 7, 8, 9, 10}

print(sec1.union(sec2))
print(sec1.intersection(sec2))
