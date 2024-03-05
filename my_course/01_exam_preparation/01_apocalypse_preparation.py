from collections import deque

textiles = deque([int(x) for x in input().split()])  # queue
medicaments = deque([int(x) for x in input().split()]) # stack

healing_items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100
}

created_healing_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    their_sum = current_textile + current_medicament

    for item, value in healing_items.items():
        if value == their_sum:
            created_healing_items[item] += 1
            break
    else:
        if their_sum > 100:
            created_healing_items['MedKit'] += 1
            their_sum -= 100
            medicaments[-1] += their_sum
        else:
            current_medicament += 10
            medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print('Textiles are empty.')
    if not medicaments:
        print('Medicaments are empty.')

sorted_created_healing_items = sorted(created_healing_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for item, value in sorted_created_healing_items:
    if value != 0:
        print(f'{item} - {value}')

# sorted_medicaments = sorted(medicaments, key= lambda x: -x)
if medicaments:
    print(f'Medicaments left: ', end='')
    print(*medicaments, sep=', ')

# sorted_textiles = sorted(textiles, key= lambda x: -x)
if textiles:
    print(f'Textiles left: ', end='')
    print(*textiles, sep=', ')
