from collections import deque

chocolate = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))
milkshakes = 0

while cups_of_milk and chocolate and milkshakes < 5:
    if chocolate[-1] <= 0 or cups_of_milk[0] <= 0:
        if chocolate[-1] <= 0:
            chocolate.pop()
        if cups_of_milk[0] <= 0:
            cups_of_milk.popleft()
        continue

    if chocolate[-1] == cups_of_milk[0]:
        cups_of_milk.popleft()
        chocolate.pop()
        milkshakes += 1
    else:
        cups_of_milk.rotate(-1)
        chocolate[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: ", end='')
    print(*chocolate, sep=', ')
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: ", end='')
    print(*cups_of_milk, sep=', ')
else:
    print("Milk: empty")

# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55

# -10, -2, -30, -10
# -5

# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
