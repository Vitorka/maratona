import itertools as it

test_cases = int(input())

for i in range(0, test_cases):

    price = int(input())

    n = int(input())

    coins = []
    for j in range(0, n):
        coins.append(int(input()))

    combinations = []

    for k in range(1, n + 1):

        aux = list(it.combinations(coins, r=k))
        combinations += aux

    sums = [sum(x) for x in combinations]

    sums.sort()

    print(combinations)

    for k in range(0, len(sums)):

        if(sums[k] >= price):
            print(sums[k], k)
            break
