a = 1
del a
# print(a)

a = [1, 2, 3, 4, 5]
# del (remove item by index)
del a[2]
print(a)

# remove by value
a.remove(5)
print(a)

# pop
print(a.pop(-1))
print(a)
