from collections import deque

parentheses = deque(input())
opening_brackets = '([{'
closing_brackets = ')]}'
counter = 0

while parentheses and counter < len(parentheses) / 2:
    if parentheses[0] not in opening_brackets:
        break
    index = opening_brackets.index(parentheses[0])
    if parentheses[1] == closing_brackets[index]:
        parentheses.popleft()
        parentheses.popleft()
        parentheses.rotate(counter)
        counter = 0
    else:
        parentheses.rotate(-1)
        counter += 1

if parentheses:
    print('NO')
else:
    print('YES')

