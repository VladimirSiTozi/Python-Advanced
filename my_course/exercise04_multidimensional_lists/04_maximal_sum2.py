rows, cols = [int(x) for x in input().split()]

matrix = [[int(i) for i in input().split()] for j in range(rows)]

max_matrix_sum = 0
max_row = 0
max_col = 0

for row in range(len(matrix) - 2):
    for col in range(len(matrix[row]) - 2):
        sub_matrix_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                sub_matrix_sum += matrix[r][c]

        if sub_matrix_sum > max_matrix_sum:
            max_matrix_sum = sub_matrix_sum
            max_row = row
            max_col = col


print(f"Sum = {max_matrix_sum}")

max_sub_matrix = [matrix[r][max_col:max_col +3]for r in range(max_row, max_row + 3)]
[print(*row)for row in max_sub_matrix]

