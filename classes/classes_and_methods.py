def test():
    pass


# a = test
# a.another_attribute = 10


def add(a, b):
    return a + b


class Test:
    def __init__(self, add_function):
        self.add_function = add_function


print(dir(test))
test = Test(add_function=add)
print(test.add_function(5, 7))

# exercise


class Monster():
    def __init__(self, func):
        self.func = func


class Attack():
    def bite():
        print('Monster bites!')

    def strike():
        return 'Monster strikes!'

    def slash():
        return 'Monster slashes!'

    def kick():
        return 'Monster kicks!'


monster = Monster(func=Attack.bite())
