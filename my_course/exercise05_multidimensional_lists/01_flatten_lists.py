# initial_list = [x.split() for x in input().split('|')]

string = input().split('|')

matrix = []

for i in range(len(string)-1, -1, -1):
    row = [x for x in string[i].split()]
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, sep=' ', end=' ')