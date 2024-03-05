import string

with open('text.txt', 'r') as input_file:
    for line, text in enumerate(input_file.readlines()):
        letters_count = 0
        punc_count = 0
        for ch in text:
            if ch.isalpha():
                letters_count += 1
            elif ch in string.punctuation:
                punc_count += 1
        with open('output.txt', 'a') as file:
            file.write(f'Line {line + 1}: {text.strip()} ({letters_count})({punc_count})\n')