line = input().split()

while(line[0] != '0' or line[1] != '0'):

    x = int(line[0])
    y = int(line[1])

    if(x + y == 13):
        print('Never speak again.')
    elif(y > x):
        print('Left beehind.')
    elif(x > y):
        print('To the convention.')
    elif(x == y):
        print('Undecided.')

    line = input().split()