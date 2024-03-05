from collections import deque

order = deque(input().split(', '))

N_ROWS, M_COLS = 6, 6
matrix = []

for r in range(N_ROWS):
    elements = [x for x in input().split()]
    matrix.append(elements)

moves_to_skip = []
move = 0

while True:

    positions = [x for x in input()]
    row = int(positions[1])
    col = int(positions[-2])
    player = order[0]

    if move in moves_to_skip:
        move += 1
        order.rotate()
        continue

    if matrix[row][col] == 'E':
        print(f'{player} found the Exit and wins the game!')
        break
    elif matrix[row][col] == 'T':
        print(f'{player} is out of the game! The winner is {order[1]}.')
        break
    elif matrix[row][col] == 'W':
        print(f'{player} hits a wall and needs to rest.')
        moves_to_skip.append(move + 2)

    order.rotate()
    move += 1

# Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)

# Jerry, Tom
# . T . . . W
# . . . . T .
# . W . . . T
# . T . E . .
# . . . . . T
# . . T . . .
# (1, 1)
# (3, 0)
# (3, 3)

# Jerry, Tom
# . . . W . .
# . . T T . .
# . . . . . .
# . T . W . .
# W . . . E .
# . . . W . .
# (0, 3)
# (3, 3)
# (1, 3)
# (2, 2)
# (3, 5)
# (4, 0)
# (5, 3)
# (3, 1)
# (4, 4)
# (4, 4)
