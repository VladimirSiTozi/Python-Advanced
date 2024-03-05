from collections import deque

example_queue = deque()

example_queue.append(1)
example_queue.append(2)
example_queue.append(3)
print(example_queue)

while example_queue:
    print(example_queue.popleft())