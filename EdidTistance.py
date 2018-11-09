number_test = int(input())

for i in range(0, number_test):

    str1 = input()
    str2 = input()

    matrix = [[0 for x in range(0, len(str2) + 1)] for y in range(0, len(str1) + 1)]

    for x in range(0, len(str1) + 1):
        matrix[x][0] = x
    for y in range(0, len(str2) + 1):
        matrix[0][y] = y


    for y in range(1, len(str2) + 1):

        for x in range(1, len(str1) + 1):

            if(str1[x - 1] == str2[y - 1]):
                cost = 0
            else:
                cost = 1

            matrix[x][y] = min(matrix[x - 1][y] + 1, matrix[x][y - 1] + 1, matrix[x - 1][y - 1] + cost)


    print(matrix[len(str1)][len(str2)])
