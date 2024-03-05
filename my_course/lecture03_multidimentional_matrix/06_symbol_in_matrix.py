n = int(input())
matrix = []
found = False

for _ in range(n):
    elements = [x for x in input()]
    matrix.append(elements)

wanted_symbol = input()

for row in range(len(matrix)):
    for col_index in range(len(matrix[row])):
        element = matrix[row][col_index]
        if element == wanted_symbol:
            found = True
            print(f"({row}, {col_index})")
            break
        if found:
            break

if not found:
    print(f'{wanted_symbol} does not occur in the matrix')

# 3
# ABC
# DEF
# X!@
# !

# 4
# asdd
# xczc
# qwee
# qefw

