# Read the number of inputs
n = int(input())

for i in range(0, n):
    line = input()

    salaries = list((map(int, line.split())))
    salaries.sort()

    print("Case {}: {}".format((i + 1), salaries[1]))
