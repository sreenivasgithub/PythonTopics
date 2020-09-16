# read a file line by line and store it into a list

def readfile(file):
    list = []
    with open(file, 'r') as f:
        FileLines = 0
        for i in f:
            list.append(i)
            #print(i, end='')
        print(list)
obj = readfile('textdata.txt')
