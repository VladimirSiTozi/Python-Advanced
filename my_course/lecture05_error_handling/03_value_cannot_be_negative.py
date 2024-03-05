class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    try:
        number = float(input())
        if number < 0:
            raise ValueCannotBeNegative
    except ValueCannotBeNegative:
        print('Value cannot be negative')
