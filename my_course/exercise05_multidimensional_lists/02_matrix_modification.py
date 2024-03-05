n = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(n)]

command = input()
while command != 'END':
    current_operation, *coordinates = command.split()
    row = int(coordinates[0])
    col = int(coordinates[1])
    value = int(coordinates[2])
    if 0 <= row < n and 0 <= col < n:
        if current_operation == 'Add':
            matrix[row][col] += value
        elif current_operation == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
    command = input()

for el in matrix:
    print(*el)


# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
