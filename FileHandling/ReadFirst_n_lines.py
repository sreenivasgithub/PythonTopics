# Write a Python program to read first n lines of a file

def firstNlines(file, n):
    with open(file, 'r') as f:
        readL = f.readlines()
    #print(readL)
    len_readL = len(readL)
    for i in range(n):
        print(readL[i], end='')

obj = firstNlines('textdata.txt', 2)