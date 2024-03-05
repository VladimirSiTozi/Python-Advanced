def sum_nums(a, b):
    return a + b


def subtract_nums(a, b):
    return a - b


sign = input()
num1 = int(input())
num2 = int(input())

mapper = {'+': sum_nums, '-': subtract_nums}

print(mapper[sign](num1, num2))

# +
# 1
# 9

# -
# 8
# 2
