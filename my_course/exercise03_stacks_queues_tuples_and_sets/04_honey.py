from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())
total_honey = 0

while working_bees and nectar:
    # step one
    if nectar[-1] >= working_bees[0]:
        # step two
        if symbols[0] == '+':
            honey_made_from_the_bee = working_bees[0] + nectar[-1]

        elif symbols[0] == '-':
            honey_made_from_the_bee = working_bees[0] - nectar[-1]

        elif symbols[0] == '*':
            honey_made_from_the_bee = working_bees[0] * nectar[-1]

        elif symbols[0] == '/':
            if nectar[-1] == 0:
                nectar.pop()
                working_bees.popleft()
                symbols.popleft()
                continue
            honey_made_from_the_bee = working_bees[0] / nectar[-1]

        total_honey += abs(honey_made_from_the_bee)
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()

    else:
        nectar.pop()
        continue

print(f'Total honey made: {total_honey}')

if not working_bees and not nectar:
    quit()
if working_bees:
    print(f"Bees left: ", end='')
    print(*working_bees, sep=', ')
else:
    print(f"Nectar left: ", end='')
    print(*nectar, sep=', ')

# 20 62 99 35 0 150
# 120 60 10 1 70 10
# / - + + / * - -

# 30
# 115
# / + + * -
