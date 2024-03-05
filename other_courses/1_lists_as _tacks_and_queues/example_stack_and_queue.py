from collections import deque

example_queue = deque()
example_stack = []

for i in range(1,6):
    example_queue.append(i)
    example_stack.append(i)

print('Queue')
print(example_queue)
while example_queue:
    print(example_queue.popleft())

print('Stack')
print(example_stack)
while example_stack:
    print(example_stack.pop())