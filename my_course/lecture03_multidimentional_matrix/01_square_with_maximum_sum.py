data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []

for rows in range(rows):
    elements = [int(i) for i in input().split(', ')]
    matrix.append(elements)

biggest_square_sum = 0
max_sum_sub_matrix = []

print(matrix)

for row_index in range(rows):
    for col_index in range(cols-1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index+1]
        element_below = matrix[row_index+1][col_index]
        next_element_below = matrix[row_index + 1][col_index+1]
        sum_elements = current_element + next_element + element_below + next_element_below
        if sum_elements > biggest_square_sum:
            biggest_square_sum = sum_elements
            max_sum_sub_matrix = [[current_element, next_element],
                                  [element_below, next_element_below]]

print(' '.join(str(i) for i in max_sum_sub_matrix[0]))
print(' '.join(str(i) for i in max_sum_sub_matrix[1]))
print(biggest_square_sum)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
#
# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
