matrix = [[int(i) for i in input().split(', ')]for j in range(int(input()))]

primary_diagonal = 0
primary_diagonal_elements = []
secondary_diagonal = 0
secondary_diagonal_elements = []

for row_index in range(len(matrix)):
    current_element = matrix[row_index][row_index]
    primary_diagonal += current_element
    primary_diagonal_elements.append(current_element)

for row_index in range(len(matrix)):
    current_element = matrix[row_index][len(matrix) - row_index - 1]
    secondary_diagonal += current_element
    secondary_diagonal_elements.append(current_element)

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal_elements)}. Sum: {primary_diagonal}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal_elements)}. Sum: {secondary_diagonal}')
