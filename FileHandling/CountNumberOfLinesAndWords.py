f = open('textdata.txt', 'r')
# d = f.read()
# words = d.split()
# lines = d.splitlines()
# print(len(words))
# print(len(lines))

cl = cw = cc = 0
for line in f:
    cl += 1
    word = line.split()
    cw += len(word)
    cc += len(line)
print('lines:',cl,'\nwords:',cw,'\ncharactors:',cc)