from collections import deque

initial_string = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"],
                    "purple": ["red", "blue"],
                    "green": ["blue", "yellow"]}

collected_colors = []

while initial_string:
    first_str = initial_string.popleft()
    last_str = initial_string.pop() if initial_string else ''

    if first_str + last_str in main_colors or first_str + last_str in secondary_colors:
        collected_colors.append(first_str + last_str)

    elif last_str + first_str in main_colors or last_str + first_str in secondary_colors:
        collected_colors.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            initial_string.insert(len(initial_string) // 2, first_str[:-1])
        if len(last_str) > 1:
            initial_string.insert(len(initial_string) // 2, last_str[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)

# d yel blu e low redd

# re ple blu pop e pur d
