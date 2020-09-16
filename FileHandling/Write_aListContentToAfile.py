# Write a List content to a file
colors = ['red', 'blue', 'green', 'yellow']
def list(file):
    with open(file, 'w') as f:
        for color in colors:
            f.write('%s\n' %color)
    r = open(file)
    return r.read()

print(list('textdata.txt'))