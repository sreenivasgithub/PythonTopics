a = int(input('Enter a number: '))
for i in range(2,a):
    if a%i == 0:
        print('Not Prime')
        break
else:
    print('Prime')

