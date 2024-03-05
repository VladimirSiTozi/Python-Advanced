n = 5
matrix = []

my_position = []
targets = 0
targets_hit = []

for r in range(n):
    matrix.append([x for x in input().split()])
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'A':
            my_position = [r, c]
        elif matrix[r][c] == 'x':
            targets += 1

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

x = int(input())

for _ in range(x):
    if len(targets_hit) == targets:
        break
    command = input().split()
    if command[0] == 'shoot':
        move = possible_moves[command[1]]
        row = my_position[0] + move[0]
        col = my_position[1] + move[1]

        while 0 <= row < n and 0 <= col < n:
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                targets_hit.append([row, col])
                break
            row += move[0]
            col += move[1]

    elif command[0] == 'move':
        move = possible_moves[command[1]]
        steps = int(command[2])
        row = my_position[0] + move[0] * steps
        col = my_position[1] + move[1] * steps
        if row < 0 or row >= n or col < 0 or col >= n:
            continue
        elif matrix[row][col] == 'x':
            continue
        matrix[row][col] = '.'
        my_position[0] = row
        my_position[1] = col

if len(targets_hit) == targets:
    print(f'Training completed! All {targets} targets hit.')
else:
    print(f'Training not completed! {targets - len(targets_hit)} targets left.')

print(*targets_hit, sep='\n')


# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1

# . . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right

# . . . . .
# . . . . .
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move right 2
# shoot left
