def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        area_result = length * width
        return f'Rectangle area: {area_result}'

    def perimeter():
        perimeter_result = (length + width) * 2
        return f'Rectangle perimeter: {perimeter_result}'

    result = f'{area()}\n{perimeter()}'
    return result


print(rectangle(2, 10))
print()
print(rectangle('2', 10))


