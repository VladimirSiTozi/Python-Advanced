from collections import deque

my_clothes_stack = deque([int(x) for x in input().split()])
rack_capacity = int(input())
racks_counter = 0


while my_clothes_stack:
    racks_counter += 1
    current_rack_capacity = rack_capacity
    while my_clothes_stack and my_clothes_stack[-1] <= current_rack_capacity:
        current_rack_capacity -= my_clothes_stack.pop()

print(racks_counter)

# 5 4 8 6 3 8 7 7 9
# 16
