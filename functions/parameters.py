def test_function(arg1, arg2, arg3, arg4):
    print(arg1, arg2, arg3, arg4)


test_function(1, arg2='hello', arg3=True, arg4=['1', 2, 'test'])

# exercise
# create greeter function with 3 arguments: person, greet and weekday
# person and greet should have default arguments ('person' for person and 'hello' for greet)
# inside of the function use a f string to print the greet and the person and also print the weekday
# when calling the function , use at least one positional argument and 1 keyword argument


def greeter(person='Person', greet='Hello', weekday=''):
    print(f'{greet} {weekday} {person}')


greeter('John', weekday='Monday')

# list unpacking


def print_all(first, *arguments, extra):
    print(first)
    print(arguments)
    print(extra)
    for arg in arguments:
        print(arg)


print_all(1, 24, True, 'yes', extra=10)

# keyword unpacking


def print_more(**arguments):
    print(arguments)


print_more(arg1=1, arg2=False, arg3='test')


def print_even_more(*args, **kwargs):
    print(args)
    print(kwargs)


print_even_more(1, 4, 53, 'base', True, [12, 53], arg1=3, arg2=False)

# exercise
# create a caculator function that prints the sum of an unlimited amount of numbers


def calculator(*args):
    result = sum(args)
    print(result)


calculator(1, 2, 56, 7, 32)
