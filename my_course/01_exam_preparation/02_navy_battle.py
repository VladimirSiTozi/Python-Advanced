N_ROWS = int(input())

CRUISERS = 3
matrix = []
submarine_position = 0, 0
hit_mines = 0
hit_cruisers = 0

for r in range(N_ROWS):
    elements = [x for x in input()]
    matrix.append(elements)
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'S':
            submarine_position = [r, c]


def is_valid_location(current_row, current_col):
    if 0 <= current_row < N_ROWS and 0 <= current_col < N_ROWS:
        return True
    return False


possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

while hit_mines != 3 and hit_cruisers != CRUISERS:
    command = input()

    move = possible_moves[command]
    current_row = submarine_position[0]
    current_col = submarine_position[1]

    desired_row = current_row + move[0]
    desired_col = current_col + move[1]

    if is_valid_location(desired_row, current_col):
        if matrix[desired_row][desired_col] == '*':
            hit_mines += 1
        elif matrix[desired_row][desired_col] == 'C':
            hit_cruisers += 1
        matrix[current_row][current_col] = '-'
        matrix[desired_row][desired_col] = 'S'
        submarine_position = [desired_row, desired_col]

    else:
        continue

if hit_cruisers == CRUISERS:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
if hit_mines == 3:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!')

[print(*row, sep='') for row in matrix]
