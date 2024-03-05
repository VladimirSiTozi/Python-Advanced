def concatenate(*args, **kwargs):
    result = ''
    for strings in args:
        result += strings

    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key, value)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print()
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
