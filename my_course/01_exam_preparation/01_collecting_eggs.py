from collections import deque

eggs = deque(int(x) for x in input().split(', '))  # queue
piece_of_paper = deque(int(x) for x in input().split(', '))  # stack

boxes = 0

while eggs and piece_of_paper:
    current_egg = eggs.popleft()
    if current_egg < 0:
        continue
    elif current_egg == 13:
        piece_of_paper[0], piece_of_paper[-1] = piece_of_paper[-1], piece_of_paper[0]
        continue
    current_paper = piece_of_paper.pop()
    their_sum = current_egg + current_paper

    if their_sum <= 50:
        boxes += 1

if boxes > 0:
    print(f'Great! You filled {boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: ', end='')
    print(*eggs, sep=', ')
if piece_of_paper:
    print(f'Pieces of paper left: ', end='')
    print(*piece_of_paper, sep=', ')


# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9

# 2, 4, 7, 8, 0
# 5, 6, 2

# 12, 23
# 28, 40
