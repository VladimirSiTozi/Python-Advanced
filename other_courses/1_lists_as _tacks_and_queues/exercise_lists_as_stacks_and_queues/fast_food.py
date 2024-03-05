from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in range(len(orders)):
    food_order = orders[0]
    if food_order <= food:
        orders.popleft()
        food -= food_order
    else:
        print('Orders left: ', end="")
        print(*orders, sep=" ")
        break

else:
    print('Orders complete')

# or
# for order in range(len(orders)):
#     food_left = orders[0]
#     if order <= food:
#         orders.popleft()
#         food -= food_left
#     else:
#         break
#
# if orders:
#     print('Orders left: ', end="")
#     print(*orders, sep=" ")
# else:
#     print('Orders complete')

# test input
# 499
# 57 45 62 70 33 90 88 76 100 50
#
# 348
# 20 54 30 16 7 9
