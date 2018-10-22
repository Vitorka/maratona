def erasthotenes(n):

    #Create a list of True, tha will be modified to inidicate if a number is prime or not
    primes = []
    for i in range(0, n+1):
        primes.append(True)

    #Two is the first prime number
    prime_number = 2

    while(prime_number*prime_number <= n+1):

        if(primes[prime_number] == True):

            #If a number is prime, retire all the numbers that are increments of the prime number
            for i in range(2* prime_number, n+1, prime_number):
                primes[i] = False

        prime_number += 1

    return primes

n = 1000000
primes = erasthotenes(n)

number = int(input())

while(number != 0):

    flag = 0

    for i in range(2, number):

        if(primes[i] == True):

            a = i
            b = number - a

            if(primes[b] == True):

                print('{} = {} + {}'.format(number, a, b))
                flag = 1
                break

    if(flag == 0):
        print('Goldbach\'s conjecture is wrong.')

    number = int(input())

