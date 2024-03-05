clothes = [int(n) for n in input().split()]
rack_space = int(input())

racks_counter = 1
current_rack = rack_space

while clothes:
    cloth = clothes.pop()

    if current_rack - cloth >= 0:
        current_rack -= cloth
    else:
        racks_counter += 1
        current_rack = rack_space - cloth

print(racks_counter)

# 5 4 8 6 3 8 7 7 9
# 16
#
# 1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
# 20
