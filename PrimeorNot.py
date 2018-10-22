import random

def modular_exponential(a, d, n):

    if(d == 0):
        return 1

    if(a == 0):
        return 0

    #Verify if d is even
    if(d % 2 == 0):
        x = modular_exponential(a, d / 2, n)
        x = (x * x) % n
    else:
        x = modular_exponential(a, d - 1, n)
        x = ((a % n) * (x % n)) % n

    return (x + n) % n

def miller_rabin(n, d, r):

    #Choose a random number a
    a = random.randint(2, n - 2)

    x = modular_exponential(a, d, n)

    if(x == 1 or x == n - 1):
        return True

    for i in range(0, r):
        x = modular_exponential(x, x, n)

        if(x == 1):
            return False

        if(x == n - 1):
            return True

    return False

def fermat(n, k):

    # Choose a random number a
    a = random.randint(2, n - 2)

    x = modular_exponential(a, n - 1, n)

    for i in range(0, k):
        if(x != 1):
            return False

    return True


def primality(n):

    #Verify some basic tests
    if(n <= 1):
        return False
    elif(n == 2 or n == 3):
        return True
    elif(n % 2 == 0):
        return False
    else:
        # k is the number of iterating
        k = 20
        return fermat(n, k)

        # # Obtain d odd by factoring in powers of 2
        # d = n - 1
        # r = 0
        # while (d % 2 == 0):
        #     d = d / 2
        #     r = r + 1
        #
        # # k is the number of iterating
        # k = 20
        #
        # for i in range(0, k):
        #
        #     if(miller_rabin(n, d, r) == False):
        #          return False
        #
        # return True


def main():

    #Read the number of tests
    tests = int(input())

    for i in range(0, tests):

        #Read the number n to be verified
        n = int(input())

        #Verify if n is prime
        prime = primality(n)

        if(prime == True):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
