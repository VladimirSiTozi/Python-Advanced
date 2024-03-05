given_string = tuple(input())
unique_symbols = set(given_string)

for symbol in sorted(unique_symbols):
    print(f'{symbol}: {given_string.count(symbol)} time/s')