from collections import deque

rows, cols = [int(x) for x in input().split()]
string = deque(input())
matrix = []

for row in range(1, rows + 1):
    matrix.append([])
    for col in range(cols):
        if row % 2 != 0:
            matrix[row - 1].append(string[0])
            string.rotate(-1)
            continue

        matrix[row - 1].insert(0, (string[0]))
        string.rotate(-1)

[print(*row, sep='') for row in matrix]


# 5 6
# SoftUni

# 1 4
# Python
