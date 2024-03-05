from collections import deque


def base_function(my_supermarket_queue):
    while True:
        name = input()
        if name == 'End':
            return print(f'{len(my_supermarket_queue)} people remaining.')
        elif name == 'Paid':
            my_supermarket_queue = paid_function(my_supermarket_queue)
        else:
            supermarket_queue.append(name)


def paid_function(my_supermarket_queue):
    while my_supermarket_queue:
        print(my_supermarket_queue.popleft())
    return my_supermarket_queue


supermarket_queue = deque()
supermarket_queue = base_function(supermarket_queue)

# George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End
