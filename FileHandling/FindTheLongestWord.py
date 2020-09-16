# Write a python program to find the longest word

def longestWord(file):
    with open(file, 'r') as f:
        read = f.read()
        word = read.split()
        listsort = sorted(word, key=len)
        print(listsort[-1])

obj = longestWord('textdata.txt')