def even_odd_filter(**kwargs):
    new_dict = {}

    for key, numbers in kwargs.items():
        if key == 'even':
            new_dict[key] = list(filter(lambda x: x % 2 == 0, numbers))
        else:
            new_dict[key] = list(filter(lambda x: x % 2 != 0, numbers))

        sorted_dict = dict(sorted(new_dict.items()))

    return sorted_dict


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2]))