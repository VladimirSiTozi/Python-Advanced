from collections import deque

cups_queue = deque([int(x) for x in input().split()])
bottles_stack = deque([int(x) for x in input().split()])
wasted_water = 0

# filling water from the bottles to the cups
while cups_queue and bottles_stack:
    if bottles_stack[-1] >= cups_queue[0]:
        wasted_water += bottles_stack[-1] - cups_queue[0]
        cups_queue.popleft()
        bottles_stack.pop()
    else:
        cups_queue[0] -= bottles_stack[-1]
        bottles_stack.pop()

# checking what's left
if cups_queue:
    print('Cups: ', end='')
    while cups_queue:
        print(cups_queue.popleft(), end=' ')

else:
    print('Bottles: ', end='')
    while bottles_stack:
        print(bottles_stack.pop(), end=' ')

print(f'\nWasted litters of water: {wasted_water}')

# 4 2 10 5
# 3 15 15 11 6

# 1 5 28 1 4
# 3 18 1 9 30 4 5

# 10 20 30 40 50
# 20 11
