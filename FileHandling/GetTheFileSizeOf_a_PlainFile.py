# Get the file size of a plain file

# Use a library like stat.py from os module

def filesize(file):
    import os
    d = os.stat(file)
    return d.st_size

print(filesize('textdata.txt'))