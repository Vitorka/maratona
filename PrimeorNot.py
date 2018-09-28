import math as m
import random as r

def modular_exponenciation(b, e, m):
    c = 1

    b = b % m

    while(e > 0):
        if(e % 2 == 1):
            c = (c * b) % m
        e = e / 2
        b = (b**2) % m

    return c


n = int(input())

for i in range(0, n):

    number = int(input())
    k = 100
    flag = 0

    if(number == 2 or number == 3):
        print('YES')
    else:
        for i in range(0, k):
            a = r.randint(2, number - 2)

            if((modular_exponenciation(a, number - 1, number)) != 1):
                print('NO')
                flag = 1
                break;

        if(flag == 0):
            print('YES')
