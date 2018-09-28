n = int(input())

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

for i in range(0, n):
    line = input()
    numbers = list(map(int, line.split()))

    print(gcd(numbers[0], numbers[1]))
