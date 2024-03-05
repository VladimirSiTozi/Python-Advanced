from collections import deque

n = int(input())
petrol_pumps_stack = deque()
start_position = 0
stops = 0

for _ in range(n):
    amount, distance = [int(x) for x in input().split()]
    petrol_pumps_stack.append([amount, distance])

while stops <= n:
    fuel = 0
    for i in range(n):
        fuel += petrol_pumps_stack[i][0]
        destination = petrol_pumps_stack[i][1]
        if fuel < destination:
            petrol_pumps_stack.rotate(-1)
            start_position += 1
            stops += 0
            break
        fuel -= destination
        stops += 1

print(start_position)
