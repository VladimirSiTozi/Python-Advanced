import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, 'example3.txt')

# instead of this

# input_file = open(file_path, 'w')
# input_file.write('Hello')
# input_file.close()

# do this, input_file is closing automatically after the block of mode with
with open(file_path, 'w') as f:
    f.write('Hello!')