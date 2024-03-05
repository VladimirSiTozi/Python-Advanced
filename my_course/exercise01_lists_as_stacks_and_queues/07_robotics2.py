from collections import deque

products = deque()
robots = deque()
robots_data = input().split(';')
hours, minutes, seconds = [int(x) for x in input().split(':')]
start_time = seconds + (minutes * 60) + (hours * 3600)

for robot in robots_data:
    name, time = robot.split('-')
    busy_until_time = 0
    robots.append({'name': name, 'time': int(time), 'busy': busy_until_time})


command = input()
while command != 'End':
    products.append(command)
    command = input()


while products:
    start_time += 1
    current_product = products.popleft()
    is_taken = False

    for robot in robots:
        if robot['busy'] <= start_time:
            robot['busy'] = start_time + robot['time']

            seconds = start_time % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            product_time = ("%02d:%02d:%02d" % (hour, minutes, seconds))

            print(f"{robot['name']} - {current_product} [{product_time}]")
            is_taken = True
            break

    if not is_taken:
        products.append(current_product)

# ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End
