p = int(input())

for i in range(0, p):

    line = input()
    line = line.split()

    n = int(line[1])

    u = 1 + ((n - 1)*1)
    s1 = int(((1 + u)*n)/2)

    u = 1 + ((n - 1)*2)
    s2 = int(((1 + u)*n)/2)

    u = 2 + ((n - 1)*2)
    s3 = int(((2 + u)*n)/2)

    print(line[0], s1, s2, s3)
