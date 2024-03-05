def even_odd(*args):
    command = args[-1]

    if command == 'even':
        return list(filter(lambda x: x % 2 == 0, args[:-1]))
    return list(filter(lambda x: x % 2 != 0, args[:-1]))

    # even = []
    # odd = []
    #
    # for num in args[:-1]:
    #     if num % 2 == 0:
    #         even.append(num)
    #     else:
    #         odd.append(num)
    #
    # if command == 'even':
    #     return even
    # return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))