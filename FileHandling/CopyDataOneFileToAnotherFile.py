# copy the contents of a file to another file

with open('textdata.txt', 'r') as f:
    read = f.read()
    print(read)
    with open('text.txt', 'w') as fw:
        write = fw.write(read)
    with open('text.txt', 'r') as fd:
        data = fd.read()
        print(data)