from functools import reduce


def operate(operator, * args):

    def add():
        return sum(args)

    def subtract():
        return reduce(lambda a, b: a-b, args)

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def divide():
        return reduce(lambda a, b: a/b, args)

    if operator == '+':
        return add()

    elif operator == '-':
        return subtract()

    elif operator == '*':
        return multiply()

    elif operator == '/':
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 3, 4, 5))