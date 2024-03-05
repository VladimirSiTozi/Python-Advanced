from collections import deque

fuel = deque(int(x) for x in input().split())  # stack
additional_consumption = deque(int(x) for x in input().split())  # queue
fuel_needed = deque(int(x) for x in input().split())  # queue

reached_altitude = []

while fuel:
    current_fuel = fuel.pop()
    current_consumption_index = additional_consumption.popleft()
    current_fuel_needed = fuel_needed[0]

    their_subtract = current_fuel - current_consumption_index

    if their_subtract >= current_fuel_needed:
        reached_altitude.append(f'Altitude {len(reached_altitude) + 1}')
        current_fuel_needed = fuel_needed.popleft()
        print(f'John has reached: Altitude {len(reached_altitude)}')

    else:
        print(f'John did not reach: Altitude {len(reached_altitude) + 1}')
        break