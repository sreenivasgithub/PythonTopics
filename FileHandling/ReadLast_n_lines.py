# Write a Python program to read last n lines of a file

def lastNlines(n):
    with open('textdata.txt', 'r') as f:
        readL = f.readlines()
        reverse_readL = readL[::-1]
        #print(reverse_readL)
    for i in range(n):
        print(reverse_readL[i])

obj = lastNlines(2)
