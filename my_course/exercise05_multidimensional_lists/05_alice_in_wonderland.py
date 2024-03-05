n = int(input())

matrix = []
alice_position = []
ALICE = 'A'
RABBIT_HOLE = 'R'

tea_value = 0

for row in range(n):
    matrix.append([x for x in input().split()])
    for col in range(len(matrix[row])):
        if matrix[row][col] == ALICE:
            alice_position = [row, col]
            matrix[row][col] = '*'

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

while tea_value < 10:
    command = input()
    move = possible_moves[command]
    row = alice_position[0] + move[0]
    col = alice_position[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        break
    if matrix[row][col] == RABBIT_HOLE:
        matrix[row][col] = '*'
        break
    if matrix[row][col].isdigit():
        tea_value += int(matrix[row][col])
    matrix[row][col] = '*'
    alice_position = [row, col]

if tea_value >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

[print(*row)for row in matrix]

# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left

# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# left
# down
# right
