with open('text.txt', 'r') as file:
    for line, text in enumerate(file.readlines()):
        if line % 2 == 0:
            for ch in ["-", ",", ".", "!", "?"]:
                text = text.replace(ch, '@')
            print(' '.join(reversed(text.split())))