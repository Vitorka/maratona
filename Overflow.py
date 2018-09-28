import sys

line = input()
while line != "":

    string = line.split()

    if(string[1] == '+'):
        result = int(string[0]) + int(string[2])
    else:
        result =   int(string[0]) * int(string[2])

    print(line)

    if(int(string[0]) > 2147483647):
        print("first number too big")
    if(int(string[2]) > 2147483647):
        print("second number too big")
    if(result > 2147483647):
        print("result too big")

    try:
        line = input()
    except Exception as e:
        break
