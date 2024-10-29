# anticipate an error in the code
try:
    print('try')
    print(a)
    print(1/0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except NameError:
    print("Error: Variable 'a' is not defined.")
else:
    print("No errors occurred.")
finally:
    print("Finally block executed.")

# raising exception
var_must_be_string = '123'
if isinstance(var_must_be_string, str):
    print(var_must_be_string)
else:
    raise TypeError("Variable 'var_must_be_string' must be of type string.")

# assert
a = 5
assert a == 5

list = [1, 2, 3, 4, 5]
try:
    list[1]
except IndexError:
    print("Index out of range error occurred.")
else:
    print("that index exist")
finally:
    print("Finish successfully.")
