N_ROWS, M_COLS = [int(x) for x in input().split()]

matrix = []
my_position = 0, 0
moves_made = 0
touched_opponents = 0
OTHER_PLAYERS = 3

for r in range(N_ROWS):
    elements = input().split()
    matrix.append(elements)
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'B':
            my_position = [r, c]

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}


def is_valid_location(current_row, current_col):
    if 0 <= current_row < N_ROWS and 0 <= current_col < M_COLS:
        return True
    return False


command = input()
while touched_opponents != OTHER_PLAYERS:
    if command == 'Finish':
        break

    move = possible_moves[command]
    current_row = my_position[0]
    current_col = my_position[1]

    desired_row = current_row + move[0]
    desired_col = current_col + move[1]

    if is_valid_location(desired_row, desired_col):
        if matrix[desired_row][desired_col] == 'O':
            command = input()
            continue
        elif matrix[desired_row][desired_col] == 'P':
            touched_opponents += 1

        moves_made += 1
        matrix[current_row][current_col] = '-'
        matrix[desired_row][desired_col] = 'B'
        my_position = [desired_row, desired_col]

    command = input()

print('Game over!')
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
# [print(''.join(row)) for row in matrix]

