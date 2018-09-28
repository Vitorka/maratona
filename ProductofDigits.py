import math as m
from collections import Counter

n = int(input())
numbers = []

if(n == 0):
    print(10)
elif(n == 1 or n == 2 or n == 3 or n == 5 or n == 7):
    print(n)
else:
    for i in range(9, 1, -1):
        while(n % i == 0):
            numbers.append(i)
            n = n / i

    if(n > 10):
        print(-1)
    else:
        numbers.sort()
        string = list(map(str,numbers))
        result = ''.join(string)
        print(result)
