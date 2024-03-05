from collections import deque

n_lines = int(input())
numbers_stack = deque()

for n in range(n_lines):
    command = input()

    if command.startswith('1'):
        current_command, number = command.split()
        numbers_stack.append(int(number))

    elif command.startswith('2'):
        if numbers_stack:
            numbers_stack.pop()

    elif command.startswith('3'):
        if numbers_stack:
            print(max(numbers_stack))

    elif command.startswith('4'):
        if numbers_stack:
            print(min(numbers_stack))

while numbers_stack:
    if len(numbers_stack) != 1:
        print(numbers_stack.pop(), end=', ')
    else:
        print(numbers_stack.pop())