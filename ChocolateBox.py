import math as mt

line = input()
while line != '-1':

    line = line.split()
    n = int(line[0])
    m = int(line[1])

    caixas_nao_vazias = 0
    for i in range(0, m):
        caixas_nao_vazias += ((-1)**(m - i) * (mt.factorial(m) / ((m - i) * mt.factorial(m))) * (i)**n) / mt.factorial(m)

    caixas_nao_vazias *= mt.factorial(m)

    result = 1 - caixas_nao_vazias / m**n

    print(result)

    try:
        line = input()
    except Exception as e:
        break
