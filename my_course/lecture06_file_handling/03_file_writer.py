with open('my_first_file.txt', 'w') as file:
    file.write('I just created my first input_file!')

# auto closed input_file
print(file.closed)
