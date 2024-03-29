import os

while True:
    line = input()
    if line == 'End':
        break

    command, filename, *args = input().split('-')
    if command == 'Create':
        open(filename, 'w').close()
    elif command == 'Add':
        with open(filename, 'a') as file:
            file.write(f'{args[0]}')
    elif command == 'Replace':
        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print('An error occurred')
        else:
            with open(filename, 'w') as file:
                content = content.replace(args[0], args[1])
                file.write(content)
    elif command == 'Delete':
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print('An error occurred')

