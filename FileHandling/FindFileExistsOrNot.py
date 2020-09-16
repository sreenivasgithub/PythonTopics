import os, sys
a = 'textdata.txt'
if os.path.isfile(a):
    f = open('textdata.txt', 'r')
else:
    print(a, 'File not exists')
    sys.exit()

d = f.read()
print(d)
f.close()