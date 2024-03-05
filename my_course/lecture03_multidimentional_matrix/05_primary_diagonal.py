n = int(input())
matrix = []

for _ in range(n):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

sum_diagonal = 0
for row_index in range(n):
    sum_diagonal += matrix[row_index][row_index]

print(f'Primary diagonal: {sum_diagonal}')


sum_secondary = 0
for row_index in range(len(matrix)):
    sum_secondary += matrix[row_index][len(matrix) - row_index - 1]
print(sum_secondary)

# 3
# 1 2 3
# 4 5 6
# 7 8 9

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
