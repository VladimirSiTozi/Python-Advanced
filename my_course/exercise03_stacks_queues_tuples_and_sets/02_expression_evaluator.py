from collections import deque
from math import floor

string_expression = deque(input().split())
my_numbers = deque()
new_number = 0

for num in string_expression:
    if num.isdigit() or num.lstrip('-').isdigit():
        my_numbers.append(int(num))

    else:
        operator = num
        new_number = my_numbers.popleft()
        if operator == '*':
            for number in my_numbers:
                new_number *= number
            my_numbers.clear()
            my_numbers.append(new_number)

        elif operator == '+':
            for number in my_numbers:
                new_number += number
            my_numbers.clear()
            my_numbers.append(new_number)

        elif operator == '-':
            for number in my_numbers:
                new_number -= number
            my_numbers.clear()
            my_numbers.append(new_number)

        elif operator == '/':
            for number in my_numbers:
                new_number /= number
            my_numbers.clear()
            my_numbers.append(floor(new_number))

print(my_numbers.popleft())

# 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *

# 2 2 - 1 *

# 6 3 - 2 1 * 5 /
