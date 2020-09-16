# import os
# present = os.path.isfile('tex.txt')
# print(present)


try:
    with open('tex.txt', 'r') as f:
        read = f.read()
    print('File is Presented')
except Exception as e:
    print(type(e).__name__)
finally:
    print('Closed')
