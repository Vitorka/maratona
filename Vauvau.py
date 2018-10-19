dogs_times = input().split()
workers_times = input().split()

a = int(dogs_times[0])
b = int(dogs_times[1])
c = int(dogs_times[2])
d = int(dogs_times[3])

for i in range(0, 3):

    attack = 0

    # Dog 1
    j = 1
    while j < 1000:

        if((int(workers_times[i]) >= j) and (int(workers_times[i]) < j + a)):
            attack += 1
        j = j + a + b

    # Dog 2
    j = 1
    while j < 1000:

        if ((int(workers_times[i]) >= j) and (int(workers_times[i]) < j + c)):
            attack += 1
        j = j + c + d


    if(attack == 2):
        print('both')
    elif(attack == 1):
        print('one')
    else:
        print('none')
