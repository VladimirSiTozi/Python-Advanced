count_of_presents = int(input())
n_size_of_the_neighborhood = int(input())

matrix = []
santa_location = []
nice_kids = 0

SANTA = 'S'
NICE_KID = 'V'
BAD_KID = 'X'
COOKIE = 'C'

for r in range(n_size_of_the_neighborhood):
    matrix.append(input().split())
    for c in range(len(matrix[r])):
        if matrix[r][c] == SANTA:
            santa_location = [r, c]
        elif matrix[r][c] == NICE_KID:
            nice_kids += 1


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

presents_left = count_of_presents
nice_kids_left = nice_kids

while nice_kids_left > 0 and presents_left > 0:
    command = input()
    if command == 'Christmas morning':
        break
    move = directions[command]
    matrix[santa_location[0]][santa_location[1]] = '-'
    row = santa_location[0] + move[0]
    col = santa_location[1] + move[1]

    if matrix[row][col] == NICE_KID:
        presents_left -= 1
        nice_kids_left -= 1
        matrix[row][col] = 'S'

    elif matrix[row][col] == BAD_KID:
        matrix[row][col] = 'S'

    elif matrix[row][col] == COOKIE:
        for happy_santa in directions.values():
            new_row = row + happy_santa[0]
            new_col = col + happy_santa[1]
            if matrix[new_row][new_col] == NICE_KID:
                presents_left -= 1
                nice_kids_left -= 1
            elif matrix[new_row][new_col] == BAD_KID:
                presents_left -= 1
            matrix[new_row][new_col] = '-'
        matrix[row][col] = 'S'

    santa_location[0] = row
    santa_location[1] = col

if presents_left == 0 and nice_kids_left != 0:
    print('Santa ran out of presents!')

[print(*row)for row in matrix]

if nice_kids_left == 0:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_left} nice kid/s.')
