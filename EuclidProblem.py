def euclidProblem(a, b):

    s = 0
    t = 1
    r = b

    s_old = 1
    t_old = 0
    r_old = a

    while(r != 0):

        q = int(r_old / r)
        r_old, r = r, (r_old - q * r)
        s_old, s = s, (s_old - q * s)
        t_old, t = t, (t_old - q * t)


    return s_old, t_old, r_old


line = input()
while True:

    line = line.split()
    a = int(line[0])
    b = int(line[1])
    x0, y0, d = euclidProblem(a, b)

    print(x0, y0, d)

    try:
        line = input()
    except Exception as e:
        break
