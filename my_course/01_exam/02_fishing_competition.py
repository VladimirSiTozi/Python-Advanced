N_ROWS = int(input())

matrix = []
my_location = 0, 0
collected_fish = 0
ship_is_sank = False

for r in range(N_ROWS):
    elements = [x for x in input()]
    matrix.append(elements)
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'S':
            my_location = [r, c]


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

command = input()
while command != 'collect the nets':
    move = possible_moves[command]

    current_row = my_location[0]
    current_col = my_location[1]

    desired_row = current_row + move[0]
    desired_col = current_col + move[1]

    if is_valid_location(desired_row, desired_col):
        if matrix[desired_row][desired_col].isdigit():
            collected_fish += int(matrix[desired_row][desired_col])
        elif matrix[desired_row][desired_col] == 'W':
            collected_fish = 0
            ship_is_sank = True
            my_location = [desired_row, desired_col]
            break

    else:
        if command == 'right':
            my_location = [desired_row, 0]
        elif command == 'left':
            my_location = [desired_row, N_ROWS]
        elif command == 'down':
            my_location = [0, desired_col]
        elif command == 'up':
            my_location = [N_ROWS, desired_col]

        if matrix[my_location[0]][my_location[1]].isdigit():
            collected_fish += int(matrix[my_location[0]][my_location[1]])
        elif matrix[my_location[0]][my_location[1]] == 'W':
            collected_fish = 0
            ship_is_sank = True
            my_location = [matrix[my_location[0]][my_location[1]]]
            break

        matrix[current_row][current_col] = '-'
        matrix[my_location[0]][my_location[1]] = 'S'
        command = input()
        continue

    matrix[current_row][current_col] = '-'
    matrix[desired_row][desired_col] = 'S'
    my_location = [desired_row, desired_col]
    command = input()

if ship_is_sank:
    print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
          f'Last coordinates of the ship: [{my_location[0]},{my_location[1]}]')

else:
    if collected_fish >= 20:
        print('Success! You managed to reach the quota!')
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! "
              f"You need {20 - collected_fish} tons of fish more.")

    if collected_fish > 0:
        print(f"Amount of fish caught: {collected_fish} tons.")
    [print(*row, sep='') for row in matrix]