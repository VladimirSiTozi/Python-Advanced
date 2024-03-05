rows, cols = [int(x) for x in input().split()]

matrix = [[i for i in input().split()]for j in range(rows)]

wanted_matrix = 0

for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        below_next_element = matrix[row_index + 1][col_index + 1]

        if current_element == next_element and current_element == below_element \
                and current_element == below_next_element:
            wanted_matrix += 1

print(wanted_matrix)

# 3 4
# A B B D
# E B B B
# I J B B

# 2 2
# a b
# c d

# 5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
