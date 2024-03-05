test_list = [1, 2, 3]

try:
    print(test_list[8])
except Exception as e:
    print(f'We have this error: {e}')
    print(f'Error type: {type(e)}')
finally:
    print('Program finished')