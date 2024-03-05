N_ROWS, M_COLS = [int(x) for x in input().split()]

matrix = []
delivery_boy_location = 0, 0
starting_position = 0, 0
pizza_is_delivered = False


for r in range(N_ROWS):
    elements = [x for x in input()]
    matrix.append(elements)
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'B':
            delivery_boy_location = [r, c]
            starting_position = [r, c]

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


while not pizza_is_delivered:
    command = input()
    move = possible_moves[command]
    current_row = delivery_boy_location[0]
    current_cow = delivery_boy_location[1]

    desired_row = delivery_boy_location[0] + move[0]
    desired_col = delivery_boy_location[1] + move[1]

    if is_valid_location(desired_row, desired_col):
        if matrix[desired_row][desired_col] == 'P':
            print("Pizza is collected. 10 minutes for delivery.")
            matrix[desired_row][desired_col] = 'R'

        elif matrix[desired_row][desired_col] == '*':
            continue

        elif matrix[desired_row][desired_col] == 'A':
            matrix[desired_row][desired_col] = 'P'
            print("Pizza is delivered on time! Next order...")
            pizza_is_delivered = True

        elif matrix[desired_row][desired_col] == '-':
            matrix[desired_row][desired_col] = '.'

        delivery_boy_location = [desired_row, desired_col]

    else:
        print("The delivery is late. Order is canceled.")
        matrix[starting_position[0]][starting_position[1]] = ' '
        break

[print(''.join(row)) for row in matrix]
