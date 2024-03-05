from collections import deque

numbers_stack = deque(input().split())

while numbers_stack:
    print(numbers_stack.pop(), end=' ')