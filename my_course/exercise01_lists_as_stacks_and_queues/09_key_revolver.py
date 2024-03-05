from collections import deque

price_of_a_bullet = int(input())
gun_barrel_size = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
value_of_the_intelligence = int(input())
counter = 0

total_bullets = len(bullets)

while locks:
    if locks[0] >= bullets[-1]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')
    bullets.pop()

    if not bullets:
        break

    counter += 1

    if counter == gun_barrel_size:
        print('Reloading!')
        counter = 0

if not locks:
    bullet_fired = total_bullets - len(bullets)
    spend_for_bullets = bullet_fired * price_of_a_bullet
    value_of_the_intelligence -= spend_for_bullets
    print(f'{len(bullets)} bullets left. Earned ${value_of_the_intelligence}')
elif locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")


# 50
# 2
# 11 10 5 11 10 20
# 15 13 16
# 1500

# 20
# 6
# 14 13 12 11 10 5
# 13 3 11 10
# 800

# 33
# 1
# 12 11 10
# 10 20 30
# 100

