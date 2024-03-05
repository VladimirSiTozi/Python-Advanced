from collections import deque

green_light_secs = int(input())
free_window_secs = int(input())

cars_queue = deque()
cars_passed = 0
free_window = free_window_secs

while True:
    car = input()

    if car == 'END':
        break
    elif car == 'green':
        for current_car in car:
            free_window -= len(current_car)
            if free_window > 0:
                cars_passed += 1

    cars_queue.append(car)

# nope
