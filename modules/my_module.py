def test_function():
    print("this is imported function")


class Test:
    def __init__(self):
        self.name = 'app'
        self.value = 12

    def do_something(self):
        print('hello')


def sum_calculator(*nums):
    return sum(nums)
