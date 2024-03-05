rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        index1 = chr(row + 97)
        index2 = chr(col + row + 97)
        index3 = index1
        element = index1 + index2 + index3
        matrix[row].append(element)

for el in matrix:
    print(*el)