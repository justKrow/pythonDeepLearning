# exercise
# create 2 global variables called 'multiplier' and has_calculated
# multiplier should have any integer and has_calculated should be set to the boolean false

# then create a function called multiply_calculator that take one argument and calculates
# the multiplication of that number
# inside of the function multiply the parameter with the global variable multiplier
# once the calculation is done set has_calculated to true
# store that new number a variable called result and return it
# print the return value of the function (after it was called the number)

multiplier = 4
has_calculated = False


def multiply_calculator(num):
    global has_calculated
    result = num * multiplier
    has_calculated = True
    return result


print(multiply_calculator(1))
print(has_calculated)
