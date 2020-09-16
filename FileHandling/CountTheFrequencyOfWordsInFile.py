# Count the frequency of words in a file
from collections import Counter
def number_of_words(file):
    with open(file, 'r') as f:
        print (Counter(f.read().split()))

obj = number_of_words('textdata.txt')