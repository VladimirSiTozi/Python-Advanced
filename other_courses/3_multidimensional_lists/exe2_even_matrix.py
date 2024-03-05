rows = int(input())
matrix = []

for row in range(int(rows)):
    current_row = [int(element) for element in input().split(', ') if int(element) % 2 == 0]
    matrix.append(current_row)

    # or
    # matrix.append([])
    # numbers = input().split(', ')
    # for number in numbers:
    #     if int(number) % 2 == 0:
    #         matrix[row].append(int(number))

print(matrix)

# 2
# 1, 2, 3
# 4, 5, 6

# 4
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67
