N_ROWS = int(input())

matrix = []
squirrel_position = 0, 0
hazelnuts = 0
break_point = False

commands = input().split(', ')

for r in range(N_ROWS):
    elements = [x for x in input()]
    matrix.append(elements)
    for c in range(len(matrix[r])):
        if matrix[r][c] == 's':
            squirrel_position = [r, c]


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

while hazelnuts != 3:
    for current_command in commands:
        move = possible_moves[current_command]

        current_row = squirrel_position[0]
        current_col = squirrel_position[1]

        desired_row = current_row + move[0]
        desired_col = current_col + move[1]

        if is_valid_location(desired_row, desired_col):
            if matrix[desired_row][desired_col] == 'h':
                hazelnuts += 1
                matrix[desired_row][desired_col] = '*'
                if hazelnuts == 3:
                    break_point = True
                    break

            elif matrix[desired_row][desired_col] == 't':
                print('Unfortunately, the squirrel stepped on a trap...')
                break_point = True
                break

            squirrel_position = [desired_row, desired_col]

        else:
            print('The squirrel is out of the field.')
            break_point = True
            break

    if break_point:
        break
    break


if hazelnuts == 3 and break_point == True:
    print('Good job! You have collected all hazelnuts!')
elif hazelnuts < 3 and break_point == False:
    print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {hazelnuts}')

# 5
# left, left, up, right, up, up
# **h**
# t****
# *h***
# *h*s*
# *****

# 4
# down, down, right, right
# *s*h
# ***h
# ***t
# h***

# 4
# down, down, right, right
# h***
# ***h
# *s*t
# **h*
