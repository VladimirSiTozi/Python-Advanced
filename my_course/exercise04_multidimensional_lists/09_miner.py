def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


n = int(input())
commands = input().split()

matrix = []
current_row, current_col = 0, 0
charcoals = 0
game_over = False

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 's':
            current_row, current_col = row, col
        elif matrix[row][col] == 'c':
            charcoals += 1

for command in commands:
    if command == 'up':
        if is_valid(current_row - 1, current_col, n):
            current_row -= 1
    elif command == 'down':
        if is_valid(current_row + 1, current_col, n):
            current_row += 1
    elif command == 'right':
        if is_valid(current_row, current_col + 1, n):
            current_col += 1
    elif command == 'left':
        if is_valid(current_row, current_col - 1, n):
            current_col -= 1

    if matrix[current_row][current_col] == 'e':
        print(f'Game over! ({current_row}, {current_col})')
        game_over = True
        break

    elif matrix[current_row][current_col] == 'c':
        charcoals -= 1
        matrix[current_row][current_col] = '*'
        if charcoals == 0:
            print(f'You collected all coal! ({current_row}, {current_col})')
            game_over = True
            break

if not game_over:
    print(f'{charcoals} pieces of coal left. ({current_row}, {current_col})')

# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *

# 4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *

# 6
# left left down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *
