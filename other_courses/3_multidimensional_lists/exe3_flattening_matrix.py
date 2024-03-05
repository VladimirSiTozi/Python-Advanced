matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]
flattening_matrix = []

for piece in matrix:
    flattening_matrix += piece

print(flattening_matrix)

# 2
# 1, 2, 3
# 4, 5, 6
