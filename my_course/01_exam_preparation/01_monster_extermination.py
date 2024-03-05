from collections import deque

armor_of_the_monsters = deque([int(x) for x in input().split(',')])  # queue
soldier_striking_impact = deque([int(x) for x in input().split(',')])  # stack

monsters_killed = 0

while armor_of_the_monsters and soldier_striking_impact:

    if soldier_striking_impact[-1] >= armor_of_the_monsters[0]:  # if soldier wins
        attack_power_left = soldier_striking_impact[-1] - armor_of_the_monsters[0]
        soldier_striking_impact.pop()
        armor_of_the_monsters.popleft()
        monsters_killed += 1

        if not soldier_striking_impact and attack_power_left > 0:
            soldier_striking_impact.append(attack_power_left)
        elif soldier_striking_impact:
            soldier_striking_impact[-1] += attack_power_left

    else:
        armor_of_the_monsters[0] -= soldier_striking_impact[-1]
        soldier_striking_impact.pop()
        armor_of_the_monsters.rotate(-1)

if not armor_of_the_monsters:
    print('All monsters have been killed!')
if not soldier_striking_impact:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {monsters_killed}')
