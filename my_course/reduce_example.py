from functools import reduce

nums = [1, 2, 3]

print(reduce(lambda a, b: a+b, nums)) 