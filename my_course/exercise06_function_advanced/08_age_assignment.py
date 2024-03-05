def age_assignment(*args, **kwargs):
    result = {}

    for key, value in kwargs.items():
        for name in args:
            if name.startswith(key):
                result[name] = value

    # creates an ordered list of tuples
    persons = sorted(result.items(), key=lambda x: x[0])

    final_result = []
    for name, age in persons:
        final_result.append(f"{name} is {age} years old.")
    return '\n'.join(final_result)


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
