from collections import deque

programmer_time = deque([int(x) for x in input().split()])  # queue
numbers_of_task = deque([int(x) for x in input().split()])  # stack

duckies_table = {
    'Darth Vader Ducky': (0, 60),
    'Thor Ducky': (61, 120),
    'Big Blue Rubber Ducky': (121, 180),
    'Small Yellow Rubber Ducky': (181, 240)
}

duckies_scoreboard = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while programmer_time and numbers_of_task:
    current_programmer = programmer_time.popleft()
    current_task = numbers_of_task.pop()
    calculated_value = current_programmer * current_task

    for duck, values in duckies_table.items():
        if values[0] <= calculated_value <= values[1]:
            duckies_scoreboard[duck] += 1
            break
    else:
        current_task -= 2
        numbers_of_task.append(current_task)
        programmer_time.append(current_programmer)

print(f'Congratulations, all tasks have been completed! Rubber ducks rewarded:')

for ducky, value in duckies_scoreboard.items():
    print(f'{ducky}: {value}')
