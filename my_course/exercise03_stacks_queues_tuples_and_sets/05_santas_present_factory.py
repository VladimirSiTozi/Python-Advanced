from collections import deque

# reading input values
materials_for_crafting_toy = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

# Present/Magic needed
toys = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400,
}

toys_made = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0,

}

while magic_level and materials_for_crafting_toy:
    if materials_for_crafting_toy[-1] == 0 or magic_level[0] == 0:
        if materials_for_crafting_toy[-1] == 0:
            materials_for_crafting_toy.pop()
        if magic_level[0] == 0:
            magic_level.popleft()
        continue

    their_multiplication = materials_for_crafting_toy[-1] * magic_level[0]

    # if their_multiplication == toys['Doll'] or their_multiplication == toys['Wooden train']
    #   or their_multiplication == toys['Teddy bear'] or their_multiplication == toys['Bicycle']:
    # same statement as the above ^
    if any(their_multiplication == price for price in toys.values()):
        if their_multiplication == toys['Doll']:
            toys_made['Doll'] += 1
        elif their_multiplication == toys['Wooden train']:
            toys_made['Wooden train'] += 1
        elif their_multiplication == toys['Teddy bear']:
            toys_made['Teddy bear'] += 1
        elif their_multiplication == toys['Bicycle']:
            toys_made['Bicycle'] += 1
        materials_for_crafting_toy.pop()
        magic_level.popleft()
        continue

    elif their_multiplication < 0:
        their_sum = materials_for_crafting_toy[-1] + magic_level[0]
        materials_for_crafting_toy.pop()
        magic_level.popleft()
        materials_for_crafting_toy.append(their_sum)
        continue

    elif their_multiplication > 0:
        magic_level.popleft()
        materials_for_crafting_toy[-1] += 15
        continue

        materials_for_crafting_toy.pop()
        magic_level.popleft()

if (toys_made['Bicycle'] > 0 and toys_made['Teddy bear'] > 0) or (toys_made['Wooden train'] > 0 and toys_made['Doll'] > 0):
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")

if materials_for_crafting_toy:
    print(f'Materials left:  {", ". join([str(x) for x in materials_for_crafting_toy[::-1]])}')

    # while materials_for_crafting_toy:
    #     print(materials_for_crafting_toy.pop(), end=', ')
    #     if len(materials_for_crafting_toy) == 1:
    #         print(materials_for_crafting_toy.pop())

if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')
    # print(*magic_level, sep=', ')

for toy, value in sorted(toys_made.items()):
    if value > 0:
        print(f'{toy}: {value}')

# 10 -5 20 15 -30 10
# 40 60 10 4 10 0

# 30 5 15 60 0 30
# -15 10 5 -15 25

# 30 10
# 15 10 5 0 10
