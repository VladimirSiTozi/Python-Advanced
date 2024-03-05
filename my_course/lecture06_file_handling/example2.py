import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, 'somefile.txt')

file = open(file_path, 'r')

# example 1
# print(input_file.read())

# example 2
# print(input_file.read(2))
# print(input_file.read(2))

# example 3
print(file.readline())

file.close()
