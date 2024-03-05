values = tuple(map(float, input().split(' ')))
counter_of_valid = {i: values.count(i) for i in values}

# for i in values:
#     if i not in counter_of_valid:
#         counter_of_valid[i] = 1
#     else:
#         counter_of_valid[i] += 1

for valid in counter_of_valid:
    print(f'{valid} - {counter_of_valid[valid]} times')

# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
#
# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
