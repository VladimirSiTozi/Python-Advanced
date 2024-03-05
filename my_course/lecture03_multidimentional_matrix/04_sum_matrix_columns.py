data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []

for i in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)


for col_index in range(cols):
    sum_cols = 0
    for row_index in range(rows):
        sum_cols += matrix[row_index][col_index]
    print(sum_cols)

# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
