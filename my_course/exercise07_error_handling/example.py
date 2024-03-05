my_test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

try:
    letter = input()
    print(my_test_dict[letter])
except KeyError:
    print('The letter is out of scope!')
else:
    print('No Errors')
finally:
    print('Program finished')