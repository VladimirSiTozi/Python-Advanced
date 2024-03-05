def print_func(not_arrived_guests):
    print(len((guests_not_on_the_party)))
    for guest in sorted(guests_not_on_the_party):
        print(guest)


invited_guests = {input() for _ in range(int(input()))}
came_guests = set()

while True:
    guest = input()
    if guest == 'END':
        break
    else:
        came_guests.add(guest)

guests_not_on_the_party = invited_guests.difference(came_guests)
print_func(guests_not_on_the_party)


# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END

# 6
# m8rfQBvl
# fc1oZCE0
# UgffRkOn
# 7ugX7bm0
# 9CQBGUeJ
# 2FQZT3uC
# 2FQZT3uC
# 9CQBGUeJ
# fc1oZCE0
# END
