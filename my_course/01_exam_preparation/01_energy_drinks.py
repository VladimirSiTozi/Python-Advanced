from collections import deque

milligrams_of_caffeine = deque(int(x) for x in input().split(', '))  # stack
energy_drinks = deque(int(x) for x in input().split(', '))  # queue

MAXIMUM_CAFFEINE = 300
total_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    current_milligrams = milligrams_of_caffeine.pop()
    current_drink = energy_drinks.popleft()

    their_sum = current_milligrams * current_drink

    if total_caffeine + their_sum <= 300:
        total_caffeine += their_sum
    else:
        energy_drinks.append(current_drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if energy_drinks:
    print(f'Drinks left: ', end='')
    print(*energy_drinks, sep=', ')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')
