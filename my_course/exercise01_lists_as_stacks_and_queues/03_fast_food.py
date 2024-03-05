from collections import deque

food_for_the_day = int(input())
food_orders_queue = deque(int(x) for x in input().split())

print(max(food_orders_queue))

while food_orders_queue:
    if food_orders_queue[0] <= food_for_the_day:
        food_for_the_day -= food_orders_queue[0]
        food_orders_queue.popleft()
    else:
        break

if len(food_orders_queue) != 0:
    print(f'Orders left:', end=' ')
    while food_orders_queue:
        print(food_orders_queue.popleft(), end=' ')

else:
    print('Orders complete')


# 348
# 20 54 30 16 7 9

# 499
# 57 45 62 70 33 90 88 76 100 50
