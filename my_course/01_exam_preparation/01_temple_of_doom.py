from collections import deque

tools = deque([int(x) for x in input().split()])  # queue
substances = deque([int(x) for x in input().split()])  # stack
challenges = [int(x) for x in input().split()]  # list

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    calculated_value = current_tool * current_substance

    if calculated_value in challenges:
        challenges.remove(calculated_value)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if not current_substance == 0:
            substances.append(current_substance)

if not tools or not substances:
    if challenges:
        print('Harry is lost in the temple. Oblivion awaits him.')

if not challenges:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')

if tools:
    print(f'Tools: ', end='')
    print(*tools, sep=', ')

if substances:
    print(f'Substances: ', end='')
    print(*substances, sep=', ')

if challenges:
    print(f'Challenges: ', end='')
    print(*challenges, sep=', ')

# 2 4 6 8
# 11 3 5 7 9
# 24 28 18 30

# 13 7 4 22 11 15 20
# 3 2 1
# 12 10 5
