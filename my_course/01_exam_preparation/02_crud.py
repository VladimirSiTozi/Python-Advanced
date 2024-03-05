N_ROWS = 6
N_COLS = 6

matrix = []
for r in range(N_ROWS):
    elements = [x for x in input().split()]
    matrix.append(elements)

position = [x for x in input()]
my_position = [int(position[1]), int(position[-2])]

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

command = input()
while command != 'Stop':
    current_command = command.split(', ')

    move = possible_moves[current_command[1]]
    current_row = my_position[0]
    current_col = my_position[1]
    desired_row = current_row + move[0]
    desired_col = current_col + move[1]

    if current_command[0] == 'Create':
        value = current_command[2]
        if matrix[desired_row][desired_col] == '.':
            matrix[desired_row][desired_col] = value

    elif current_command[0] == 'Update':
        value = current_command[2]
        if matrix[desired_row][desired_col] != '.':
            matrix[desired_row][desired_col] = value

    elif current_command[0] == 'Delete':
        if matrix[desired_row][desired_col] != '.':
            matrix[desired_row][desired_col] = '.'

    elif current_command[0] == 'Read':
        if matrix[desired_row][desired_col] != '.':
            print(matrix[desired_row][desired_col])

    my_position = [desired_row, desired_col]

    command = input()

[print(*row) for row in matrix]

