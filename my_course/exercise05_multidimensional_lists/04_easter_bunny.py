n = int(input())
matrix = []

bunny_position = []
traps = []
possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

max_eggs = float('-inf')
max_direction = ''
max_moves = []

for row in range(n):
    elements = [x for x in input().split()]
    matrix.append(elements)
    for col in range(n):
        if matrix[row][col] == 'B':
            bunny_position = [row, col]
        elif matrix[row][col].isdigit():
            matrix[row][col] = int(matrix[row][col])
        elif matrix[row][col] == 'X':
            traps.append([row, col])


for direction, move in possible_moves.items():
    eggs = 0
    current_egg_matrix = []
    row = bunny_position[0] + move[0]
    col = bunny_position[1] + move[1]

    while row < 0 or row >= n or col < 0 or col >= n:
        if matrix[row][col] == 'X':
            break
        eggs += matrix[row][col]
        current_egg_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and current_egg_matrix:
        max_eggs = eggs
        max_direction = direction
        max_moves = current_egg_matrix


print(max_direction)
[print(row) for row in max_moves]
print(max_eggs)