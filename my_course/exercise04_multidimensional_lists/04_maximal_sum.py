rows, cols = [int(x) for x in input().split()]

matrix = [[int(i) for i in input().split()] for j in range(rows)]

max_matrix_sum = 0
max_sub_matrix = []

for row in range(len(matrix) - 2):
    for col in range(len(matrix[row]) - 2):
        element_00 = matrix[row][col]
        element_01 = matrix[row][col + 1]
        element_02 = matrix[row][col + 2]
        first_row_sum = element_00 + element_01 + element_02

        element_10 = matrix[row + 1][col]
        element_11 = matrix[row + 1][col + 1]
        element_12 = matrix[row + 1][col + 2]
        second_row_sum = element_10 + element_11 + element_12

        element_20 = matrix[row + 2][col]
        element_21 = matrix[row + 2][col + 1]
        element_22 = matrix[row + 2][col + 2]
        third_row_sum = element_20 + element_21 + element_22

        sub_matrix_sum = first_row_sum + second_row_sum + third_row_sum

        if sub_matrix_sum >= max_matrix_sum:
            max_matrix_sum = sub_matrix_sum
            max_sub_matrix.clear()
            max_sub_matrix.append([element_00, element_01, element_02])
            max_sub_matrix.append([element_10, element_11, element_12])
            max_sub_matrix.append([element_20, element_21, element_22])

print(f"Sum = {max_matrix_sum}")
print(*max_sub_matrix[0])
print(*max_sub_matrix[1])
print(*max_sub_matrix[2])

# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4

# 5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5
