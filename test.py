import fileinput

dictionary = {}
for line in fileinput.input():
    line = line.rstrip()
    if line.find(' ') != -1:
        new = line.split(maxsplit=1)
        dictionary[new[0]] = new[1]
        print(new)
    elif line.find('-') != -1:
        new = line.split('-')
        print(new)
print(dictionary.items())