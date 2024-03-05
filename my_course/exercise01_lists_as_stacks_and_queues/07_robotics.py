from collections import deque
from datetime import datetime, timedelta

initial = deque(input().split(';'))
robots = deque()

for robot in initial:
    name, time = robot.split('-')
    robots.append([name, int(time)])

initial_staring_time = input()

staring_time = datetime.strptime(initial_staring_time, "%H:%M:%S")
formatted_time = staring_time.strftime("%I:%M:%S")
print(formatted_time)

# new_time = staring_time + timedelta(seconds=56)
# formatted_time = new_time
# print(formatted_time)




