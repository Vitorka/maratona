import itertools
import numpy as np
import sys

def gdc(a, b):
    if(a % b == 0):
        return b
    else:
        return gdc(b, a % b)

n = input()
n = int(n)

for j in range(0, n):
    numbers = sys.stdin.readline()

    array = numbers.split()

    permutations = list(itertools.permutations(array, 2))

    resultado = 0
    for i in range(0, len(permutations)):
        aux = gdc(int(permutations[i][0]), int(permutations[i][1]))

        if(aux > resultado):
            resultado = aux

    print(resultado)
