line = input().split()

c = int(line[0])
n = int(line[1])

inside_train = 0
flag = 0
for i in range(0, n):

    line = input().split()

    left = int(line[0])
    entered = int(line[1])
    stay = int(line[2])

    if (left > inside_train):
        flag = 1
        break

    inside_train = inside_train - left
    if(inside_train < 0):
        flag = 1
        break

    inside_train = inside_train + entered
    if(inside_train > c):
        flag = 1
        break

    if((stay != 0) and (inside_train != c)):
        flag = 1
        break

    if(i == n - 1):
        if (stay != 0):
            flag = 1
        if (entered != 0):
            flag = 1
        if (inside_train != 0):
            flag = 1

if(flag == 0):
    print('possible')
else:
    print('impossible')