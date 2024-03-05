numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line2 = input()
while line2 != "Remove":
    searched = line2
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line2 = input()

line3 = input()
while line3 != "End":
    searched1 = line3
    try:
        del numbers_dictionary[searched1]
    except KeyError:
        print("Number does not exist in dictionary")
    line3 = input()

print(numbers_dictionary)

# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End

# one
# two
# Search
# Remove
# End

# one
# 1
# Search
# one
# Remove
# two
# End
