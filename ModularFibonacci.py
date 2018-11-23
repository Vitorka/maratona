import  math

def fibonacci(n):

    if(n == 0):
        return 0
    elif(n <= 2):
        return 1

    if(n % 2):
        b = (n - 1) / 2
        return (fibonacci(b) * fibonacci(b)) + (fibonacci(b + 1) * fibonacci(b + 1))
    else:
        b = n / 2
        return fibonacci(b) * (2 * fibonacci(b + 1) - fibonacci(b))
    # a = 0
    # b = 1
    # for i in range(1, n):
    #     aux = a + b
    #     a = b
    #     b = aux
    #
    # return b

print(fibonacci(2147483647))
# line = input().split()
#
# while True:
#
#     n = int(line[0])
#     m = int(line[1])
#
#     n = fibonacci(n)
#
#     print(n % (math.pow(2, m)))
#
#     try:
#         line = input().split()
#     except Exception as e:
#         break
