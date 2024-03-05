n_rows, m_columns = [int(x) for x in input().split(',')]

matrix = []
mouse_location = 0, 0
cheeses = 0
cheeses_eaten = 0

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}


def is_valid_location(current_row, current_col):
    if 0 <= current_row < n_rows and 0 <= current_col < m_columns:
        return True
    return False


for r in range(n_rows):
    elements = [x for x in input()]
    matrix.append(elements)
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'M':
            mouse_location = [r, c]
        elif matrix[r][c] == 'C':
            cheeses += 1

print('Feed the mouse!')

while True:
    try:
        command = input()

        if command == 'danger':
            print('Mouse will come back later!')
            break

        move = possible_moves[command]
        row = mouse_location[0] + move[0]
        col = mouse_location[1] + move[1]
        matrix[mouse_location[0]][mouse_location[1]] = '*'

        if is_valid_location(row, col):
            if matrix[row][col] == 'C':
                cheeses_eaten += 1
                mouse_location = [row, col]
                matrix[row][col] = 'M'
                if cheeses_eaten == cheeses:
                    print('Happy mouse! All the cheese is eaten, good night!')
                    break

            elif matrix[row][col] == 'T':
                mouse_location = [row, col]
                matrix[row][col] = 'M'
                print('Mouse is trapped!')
                break

            elif matrix[row][col] == '@':
                matrix[mouse_location[0]][mouse_location[1]] = 'M'
                continue

            mouse_location = [row, col]
            matrix[row][col] = 'M'
        else:
            print('No more cheese for tonight!')
            matrix[mouse_location[0]][mouse_location[1]] = 'M'
            break
        [print(''.join(row)) for row in matrix]
    except KeyError:
        print('Please give proper command')
        continue

[print(''.join(row))for row in matrix]

# 5,5
# **M**
# T@@**
# CC@**
# **@@*
# **CC*
# left
# down
# left
# down
# down
# down
# right
# danger

# 4,8
# CC@**C*M
# T*@**CT*
# **@@@@**
# T***C***
# down
# right
# left
# down
# left
# danger

# 6,3
# @CC
# @TC
# @C*
# @M*
# @**
# @**
# left
# up
# left
# right
# up
# up
# left
# left
# danger
