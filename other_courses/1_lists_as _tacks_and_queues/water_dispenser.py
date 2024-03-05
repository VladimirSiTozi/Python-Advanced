from collections import deque


def base_function(people_queue, water):

    while True:
        name = input()
        if name == COMMAND_START:
            start_function(people_queue, water)
            break
        else:
            people_queue.append(name)


def start_function(people_queue, water):
    while True:
        command = input()
        if command == COMMAND_END:
            print(f'{water} liters left')
            break
        elif command.startswith('refill'):
            action, liters = command.split()
            water += int(liters)
        else:
            if int(command) <= water:
                print(f'{people_queue.popleft()} got water')
                water -= int(command)
            else:
                print(f'{people_queue.popleft()} must wait')


my_people_queue = deque()
COMMAND_END = 'End'
COMMAND_START = 'Start'

initial_water = int(input())
base_function(my_people_queue, initial_water)


# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End

# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End
