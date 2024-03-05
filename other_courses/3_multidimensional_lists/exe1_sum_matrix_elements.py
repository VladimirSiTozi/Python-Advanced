rows, columns = input().split(', ')
matrix = []

for row in range(int(rows)):
    matrix.append([])
    for column in range(1):
        numbers = input().split(', ')
        for number in numbers:
            matrix[row].append(int(number))

sum_matrix = 0
for lst in matrix:
    sum_matrix += sum(lst)

print(sum_matrix)
print(matrix)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
