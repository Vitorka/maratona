def eratosthenes(n):

    primes = []
    for i in range(2, n):
        primes.append(True)

    return primes
    
line = input()
while line != '0':

    n = int(line)
    primes = eratosthenes(n)
    print(primes)

    line = input()
