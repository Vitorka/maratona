n = int(input())

while True:
    max = 0

    if(n < 3):
        max = 0
    else:
        max = int(1 + ((2 + (n - 2))*(n - 3)/2))

    print(max)

    try:
        n = int(input())
    except Exception as e:
        break