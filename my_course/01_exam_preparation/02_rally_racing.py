N_ROWS = int(input())

matrix = []
racing_number = input()

tunnel_location = {}
kilometers_passed = 0
car_location = [0, 0]


for r in range(N_ROWS):
    elements = [x for x in input().split()]
    matrix.append(elements)
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'T':
            key = 'T' + str(len(tunnel_location) + 1)
            tunnel_location[key] = [r, c]


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

while True:
    command = input()
    if command == 'End':
        print(f'Racing car {racing_number} DNF.')
        break

    move = possible_moves[command]
    current_row = car_location[0]
    current_col = car_location[1]

    desired_row = current_row + move[0]
    desired_col = current_col + move[1]

    if is_valid_location(desired_row, desired_col):
        if matrix[desired_row][desired_col] == '.':
            kilometers_passed += 10

        elif matrix[desired_row][desired_col] == 'T':
            for tunnel, location in tunnel_location.items():
                if [desired_row, desired_col] == location:
                    matrix[desired_row][desired_col] = '.'
                    matrix[current_row][current_col] = '.'
                    tunnel_location.pop(tunnel)
                    break
            kilometers_passed += 30
            for tunnel, location in tunnel_location.items():
                car_location = [location[0], location[1]]
                matrix[location[0]][location[1]] = 'C'
                break
            continue

        elif matrix[desired_row][desired_col] == 'F':
            print(f'Racing car {racing_number} finished the stage!')
            kilometers_passed += 10
            matrix[current_row][current_col] = '.'
            car_location = [desired_row, desired_col]
            matrix[desired_row][desired_col] = 'C'
            break

        matrix[current_row][current_col] = '.'
        car_location = [desired_row, desired_col]
        matrix[desired_row][desired_col] = 'C'

print(f'Distance covered {kilometers_passed} km.')
[print(*row, sep='') for row in matrix]
