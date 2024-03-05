from collections import deque

n = int(input())
petrol_pumps_stack = deque()
truck_capacity = 0
number_of_pump = 0
stops = 0

for _ in range(n):
    amount, distance = [int(x) for x in input().split()]
    petrol_pumps_stack.append([amount, distance])


current_petrol_pumps = petrol_pumps_stack.copy()
while current_petrol_pumps:
    truck_capacity += current_petrol_pumps[0][0]
    if current_petrol_pumps[0][1] <= truck_capacity:
        truck_capacity -= current_petrol_pumps[0][1]
        current_petrol_pumps.popleft()
        stops += 1
    else:
        truck_capacity = 0
        current_petrol_pumps = petrol_pumps_stack.copy()
        for _ in range(stops):
            current_petrol_pumps.rotate(-1)
        number_of_pump += 1
        stops = 0

print(number_of_pump)


