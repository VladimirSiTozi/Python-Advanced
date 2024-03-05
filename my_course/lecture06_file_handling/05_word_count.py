import re

with open('05_words.txt', 'r') as file:
    searched_words = file.read().lower().split()


with open('05_text.txt', 'r') as file:
    text = file.read().lower()

words = {}

for searched_word in searched_words:
    regex = re.compile(rf'\b{searched_word}\b')
    result = re.findall(regex, text)
    words[searched_word] = text.count(searched_word)


with open('05_output.txt', 'w') as file:
    for key, value in sorted(words.items(), key=lambda x: -x[-1]):
        file.write(f'{key} - {value}\n')