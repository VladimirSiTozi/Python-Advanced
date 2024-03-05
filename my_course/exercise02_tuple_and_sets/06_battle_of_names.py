n = int(input())

evens = set()
odds = set()

for row in range(1, n+1):
    sum_of_name = 0
    name = input()
    for char in name:
        sum_of_name += ord(char)

    sum_of_name = sum_of_name // row

    if sum_of_name % 2 == 1:
        odds.add(sum_of_name)
    else:
        evens.add(sum_of_name)

if sum(evens) == sum(odds):
    result = odds | evens
elif sum(evens) > sum(odds):
    result = odds ^ evens
elif sum(evens) < sum(odds):
    result = odds.difference(evens)

print(*result, sep=', ')