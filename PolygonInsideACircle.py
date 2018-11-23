import math as m

line = input().split()

while True:

    r = float(line[0])
    n = float(line[1])

    area = (1/2) * n * (r**2) * m.sin((2*m.pi)/n)

    print('{:.3f}'.format(area))

    try:
        line = input().split()
    except Exception as e:
        break