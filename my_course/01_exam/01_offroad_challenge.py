from collections import deque

fuel = deque(int(x) for x in input().split())  # stack
additional_consumption_index = deque(int(x) for x in input().split())  # queue
amount_of_fuel_needed = deque(int(x) for x in input().split())  # queue

reached_altitude = []

while fuel and additional_consumption_index:
    current_fuel = fuel.pop()
    current_consumption_index = additional_consumption_index.popleft()
    current_fuel_needed = amount_of_fuel_needed[0]

    their_subtract = current_fuel - current_consumption_index

    if their_subtract >= current_fuel_needed:
        reached_altitude.append(f'Altitude {len(reached_altitude) + 1}')
        current_fuel_needed = amount_of_fuel_needed.popleft()
        print(f'John has reached: Altitude {len(reached_altitude)}')

    else:
        print(f'John did not reach: Altitude {len(reached_altitude) + 1}')
        break


if 0 < len(reached_altitude) < 4:
    print('John failed to reach the top.')
    print(f'Reached altitudes: {", ".join(reached_altitude)}')

if len(reached_altitude) == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

if len(reached_altitude) == 4:
    print('John has reached all the altitudes and managed to reach the top!')
