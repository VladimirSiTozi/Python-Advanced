n = int(input())

longest_intersection = set()

for _ in range(n):
    left_side, right_side = input().split('-')
    left_start, left_end = left_side.split(',')
    left_sequence = set()

    for nums in range(int(left_start), int(left_end) + 1):
        left_sequence.add(nums)

    right_start, right_end = right_side.split(',')
    right_sequence = set()

    for nums in range(int(right_start), int(right_end) + 1):
        right_sequence.add(nums)

    their_intersection = left_sequence & right_sequence

    if len(their_intersection) > len(longest_intersection):
        longest_intersection = their_intersection


print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')