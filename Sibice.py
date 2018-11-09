line = input().split()

n = int(line[0])
w = int(line[1])
h = int(line[2])
diagonal = (w**2 + h**2)**(1/2)

for i in range(0, n):

    match = int(input())

    if(match <= h):
        print('DA')
    elif(match <= w):
        print('DA')
    elif(match <= diagonal):
        print('DA')
    else:
        print('NE')

