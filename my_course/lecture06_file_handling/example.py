email = input()

file = open('storage.txt', 'a')
file.write(email + '\n')

file.close()