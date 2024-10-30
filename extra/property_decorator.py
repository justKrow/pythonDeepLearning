class Generic:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        print('get x')
        return self._x

    @x.setter
    def x(self, value):
        print('set x')
        self._x = value

    @x.deleter
    def x(self):
        print('delete x')
        del self._x


generic = Generic()
generic.x = 50
print(generic.x)
del generic.x
