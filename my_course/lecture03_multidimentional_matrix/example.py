matrix = [[0 for i in range(2)]for j in range(3)]
print(matrix)

matrix1 = [[i for i in range(1,4)]for j in range(3)]
print(matrix1)

matrix2 = [[i for i in input().split(', ')]for j in range(3)]
# # 1, 2, 3
# # 1, 2, 3
# # 1, 2, 3
print(matrix2)

matrix3 = [[i for i in input().split(', ')]for j in range(int(input()))]
# 2
# 1, 2, 3
# 1, 2, 3
print(matrix3)