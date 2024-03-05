def is_valid(indexes, rows, cols):
    return 0 <= indexes[0] < rows and 0 <= indexes[2] < rows and 0 <= indexes[1] < cols and 0 <= indexes[3] < cols


rows, cols = [int(x) for x in input().split()]

matrix = [[col for col in input().split()] for row in range(rows)]

command = input()
while command != 'END':
    swap_command, *indexes = command.split()
    if swap_command == 'swap' and len(indexes) == 4:
        indexes = [int(x) for x in indexes]
        if is_valid(indexes, rows, cols):
            element01 = matrix[indexes[0]][indexes[1]]
            element02 = matrix[indexes[2]][indexes[3]]

            matrix[indexes[0]][indexes[1]] = element02
            matrix[indexes[2]][indexes[3]] = element01

            for el in matrix:
                print(*el)
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()
