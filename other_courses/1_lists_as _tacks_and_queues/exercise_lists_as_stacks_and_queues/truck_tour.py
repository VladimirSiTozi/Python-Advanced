from collections import deque

pumps = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_copy = pumps.copy()
index = 0
gas_in_tank = 0

while pumps_copy:
    petrol, distance = pumps_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank - distance < 0:
        pumps.rotate(-1)
        pumps_copy = pumps.copy()
        index += 1
        gas_in_tank = 0

    else:
        gas_in_tank -= distance

print(index)

# 3
# 1 5
# 10 3
# 3 4
#
# 5
# 22 5
# 14 10
# 52 7
# 21 12
# 36 9
