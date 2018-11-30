def fibonacci(n):

  a = 'N'
  b = 'A'

  if(n == 0):
    return 'N'
  elif(n == 1):
    return 'A'

  for i in range(1, n):
    aux = a + b
    a = b
    b = aux

  return b

line = input().split()

n = int(line[0])
k = int(line[1]) - 1

string = fibonacci(n)

print(string[k])
