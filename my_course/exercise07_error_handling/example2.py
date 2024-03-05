my_test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
test_list = [1, 2, 3]

letter = input()
try:
    print(test_list[8])
    print(my_test_dict[letter])
except KeyError:
    print('The letter is out of scope!')
except IndexError:
    print('Index Error')
else:
    print('No Errors')
finally:
    print('Program finished')