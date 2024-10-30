def func():
    print("function")


def wrapper(func):
    print('hello')
    func()
    print('bye')


def function_generator():
    def new_function():
        print('this is a new function')
    return new_function


wrapper(func)

new_func = function_generator()
new_func()
