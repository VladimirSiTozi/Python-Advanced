def accommodate_new_pets(capacity, weight_limit, *args):
    visitors = {}
    number_of_pets = 0
    ignored = 0
    for pet, weight in args:
        if weight <= weight_limit:
            if capacity > number_of_pets:
                if pet not in visitors:
                    visitors[pet] = 0
                visitors[pet] += 1
                number_of_pets += 1
                if capacity == number_of_pets:
                    break
            else:
                break
        else:
            ignored += 1

    result = ''
    if len(args) <= number_of_pets + ignored:
        result += f'All pets are accommodated! Available capacity: {capacity - number_of_pets}.'
    else:
        result += 'You did not manage to accommodate all pets!'

    result += '\nAccommodated pets:\n'

    sorted_visitors = sorted(visitors.items(), key=lambda kvp: kvp[0])
    for pet, value in sorted_visitors:
        result += f'{pet}: {value}\n'
    return result

# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))
#
# print()
# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))

# print()
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
