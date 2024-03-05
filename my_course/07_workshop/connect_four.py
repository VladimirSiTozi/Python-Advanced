from collections import deque

ROWS = 6
COLS = 7

directions_mapper = {
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (1, 0),  # left
    (-1, 1),  # up right
    (-1, -1),  # up left
    (1, 1),  # down right
    (1, -1),  # down left
}


class FullColumnError(Exception):
    pass


def print_matrix(my_matrix):
    [print(row)for row in matrix]


def is_valid_column_choice(index):
    if 0 <= index < 7:
        return True
    return False


def is_valid_place(rol, col):
    if 0 <= rol < ROWS and 0 <= col < COLS:
        return True
    return False


def selecting(selected_column_index, my_matrix):
    row = 0
    for r in range(len(matrix[selected_column_index])):

        if matrix[0][selected_column_index] != 0:
            raise FullColumnError

        if matrix[r][selected_column_index] != 0:
            matrix[r - 1][selected_column_index] = player[0]
            row = r
            break

        elif r == 5:  # ROWS -1
            matrix[r][selected_column_index] = player[0]
            break

    return row, selected_column_index


def connecting_four(my_matrix, row, col, player):
    for row_movement, col_movement in directions_mapper:
        count = 1
        for step in range(1, 4):
            row_index_to_check = row + row_movement * step
            col_index_to_check = col + col_movement * step

            if not is_valid_place(row_index_to_check, col_index_to_check):
                break

            if matrix[row_index_to_check][col_index_to_check] != player:
                break

            count += 1
        if count >= 3:
            return True
    return False


matrix = [[0 for _ in range(COLS)]for _ in range(ROWS)]
print_matrix(matrix)

player = deque([1, 2])
while True:
    try:
        selected_column_number = int(input(f'Player {player[0]}, please choose a column: '))
        selected_column_index = selected_column_number - 1
        if not is_valid_column_choice(selected_column_index):
            raise ValueError

        current_row, current_col = selecting(selected_column_index, matrix)

        if connecting_four(matrix, current_row, current_col, player[0]):
            print(f'Winner Winner Chicken Dinner! Player {player[0]} wins')
            print_matrix(matrix)
            break

        print_matrix(matrix)

    except ValueError:
        print(f'Player {player[0]} please select number between 1 and {COLS}')
        continue

    except FullColumnError:
        print(f'Player {player[0]}, this column is full, please select another one!')
        continue

    player.rotate()


# https://pastebin.com/neDaEbF2
