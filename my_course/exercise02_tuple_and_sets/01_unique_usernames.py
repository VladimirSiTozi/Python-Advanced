n = int(input())

usernames = set()

for _ in range(n):
    name = input()
    usernames.add(name)

print(*usernames, sep='\n')

# for name in usernames:
#     print(name)


# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234
