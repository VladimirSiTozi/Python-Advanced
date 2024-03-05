matrix = [[int(i) for i in input().split()]for j in range(int(input()))]

primary_diagonal = 0
secondary_diagonal = 0

for row_index in range(len(matrix)):
    y = matrix[row_index][row_index]
    primary_diagonal += y

for row_index in range(len(matrix)):
    x = matrix[row_index][len(matrix) - row_index - 1]
    secondary_diagonal += x

print(abs(primary_diagonal - secondary_diagonal))

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# 4
# -7 14 9 -20
# 3 4 9 21
