import os

files = {}
directory = '../'

for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        ext = element.split('.')[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f)
            if os.path.isfile(filename):
                ext = el.split('')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)