from collections import deque

first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

n = int(input())


def add_first(sequence, command):
    command1, command2, *nums = command.split()
    for num in nums:
        sequence.add(int(num))
    return sequence


def add_second(sequence, command):
    command1, command2, *nums = command.split()
    for num in nums:
        sequence.add(int(num))
    return sequence


def remove_first(sequence, command):
    command1, command2, *nums = command.split()
    for num in nums:
        if int(num) in sequence:
            sequence.remove(int(num))
    return sequence


def remove_second(sequence, command):
    command1, command2, *nums = command.split()
    for num in nums:
        if int(num) in sequence:
            sequence.remove(int(num))
    return sequence


def is_subset_func(first_seque, second_seque):
    result = first_seque < second_seque
    if result:
        print(result)
    result = second_seque < first_seque
    print(result)


for _ in range(n):
    current_command = input()

    if current_command.startswith('Add First'):
        add_first(first_sequence, current_command)

    elif current_command.startswith('Add Second'):
        add_second(second_sequence, current_command)

    elif current_command.startswith('Remove First'):
        remove_first(first_sequence, current_command)

    elif current_command.startswith('Remove Second'):
        remove_second(second_sequence, current_command)

    elif current_command.startswith('Check Subset'):
        is_subset_func(first_sequence, second_sequence)

print(*first_sequence, sep=', ')
print(*second_sequence, sep=', ')

# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset

# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 13
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
