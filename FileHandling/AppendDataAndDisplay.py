f = open('textdata.txt', 'a+')
f.write(' extended again')
f.seek(0,0)
d = f.read()
print(d)
f.close()