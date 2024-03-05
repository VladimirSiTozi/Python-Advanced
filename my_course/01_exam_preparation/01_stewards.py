from collections import deque

seats = deque(x for x in input().split(', '))
first_sequences = deque(int(x) for x in input().split(', '))  # queue
second_sequences = deque(int(x) for x in input().split(', '))  # stack

seats_matched = deque()
seat_matches = 0
MAX_SEAT_MATCHED = 3
rotation = 0
MAX_ROTATION = 10

while seat_matches != MAX_SEAT_MATCHED and rotation != MAX_ROTATION:
    first_num = first_sequences[0]
    second_num = second_sequences[-1]
    their_sum = first_num + second_num
    sum_ascii = chr(their_sum)
    current_seat = f'{first_num}{sum_ascii}'
    current_seat2 = f'{second_num}{sum_ascii}'

    if current_seat in seats:
        if current_seat in seats_matched:
            first_sequences.popleft()
            second_sequences.pop()
            continue
        first_sequences.popleft()
        second_sequences.pop()
        seats_matched.append(current_seat)
        seats.remove(current_seat)
        seat_matches += 1
        rotation += 1

    elif current_seat2 in seats:
        if current_seat2 in seats_matched:
            first_sequences.popleft()
            second_sequences.pop()
            continue
        first_sequences.popleft()
        second_sequences.pop()
        seats_matched.append(current_seat2)
        seats.remove(current_seat2)
        seat_matches += 1
        rotation += 1

    else:
        first_sequences.rotate(-1)
        second_sequences.rotate()
        rotation += 1

print(f'Seat matches: {", ".join(seats_matched)}')
print(f'Rotations count: {rotation}')