n, m = [int(x) for x in input().split()]

n_set = {input() for x in range(n)}
m_set = set()

# for _ in range(n):
#     n_set.add(input())

for _ in range(m):
    m_set.add(input())

a = n_set & m_set

print(*a, sep='\n')
