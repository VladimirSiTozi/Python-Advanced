from collections import deque

food_supplies = deque(int(x) for x in input().split(', '))  # stack
daily_stamina = deque(int(x) for x in input().split(', '))  # queue

mountains_order = deque(['Vihren', 'Kutelo', 'Banski Suhodol', 'Polezhan', 'Kamenitza'])
conquered_peaks = deque([])

mountain_peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70,
}

climbed_mountain_peaks = {
    'Vihren': 0,
    'Kutelo': 0,
    'Banski Suhodol': 0,
    'Polezhan': 0,
    'Kamenitza': 0,
}

while food_supplies and daily_stamina and mountains_order:
    current_food = food_supplies.pop()
    current_stamina = daily_stamina.popleft()
    current_mountain = mountains_order[0]

    their_sum = current_food + current_stamina

    if their_sum >= mountain_peaks[current_mountain]:
        climbed_mountain_peaks[current_mountain] = True
        mountains_order.popleft()
        conquered_peaks.append(current_mountain)

if not mountains_order:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered_peaks:
    print('Conquered peaks:')
    print('\n'.join(conquered_peaks))
