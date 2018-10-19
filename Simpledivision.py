def euclidian(a, b):

    if(a == 0):
        return b
    else:
        return euclidian(b % a, a)

numbers = input()

while( numbers != '0'):

    # Put all numbers in a list and remove the last number 0
    numbers = list(map(int, numbers.split()))
    numbers.remove(0)

    #Calculate the differences
    diff = []
    for i in range(0, len(numbers) - 1):

        diff.append(numbers[i + 1] - numbers[i])

    #Calculate GCD
    for i in range(0, len(diff)):
        if(i == 0):
            final = diff[i]
        else:
            final = euclidian(final, diff[i])

    if(final < 0):
        print(final * -1)
    else:
        print(final)

    numbers = input()