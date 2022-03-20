import numbers


number = int(input("ป้อนเลข"))
for row in range(number):
    for colum in range(number):
        print('x',end='')
    print('')