def grocery_store(**kwargs):
    sorted_list = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    my_list = []
    for key, value in sorted_list.items():
        my_list.append(f'{key}: {value}')

    return '\n'.join(my_list)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print()
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
