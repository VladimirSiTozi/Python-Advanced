def ages(numbers):
    min_age = min(numbers)
    max_age = max(numbers)

    return min_age, max_age


min_age, max_age = ages([1, 2, 12, 7, 52])

print(max_age)
print(min_age)