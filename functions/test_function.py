def test_function():
    print("hello")
    test = 1 + 2
    print(test)


def calculate(num1, num2):
    result = num1 + num2
    print(result)


test_function()
calculate(2, 4)


def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"
    print(result)


calculator(2, 4, '-')
