def rotaciona(matrix):

    i1 = 0
    i2 = 3
    i3 = 3
    i4 = 0
    while((i1 < 3) and (i2 > 0) and (i3 > 0) and (i4 < 3)):

        aux1 = matrix[0][i1]
        aux2 = matrix[i2][0]
        aux3 = matrix[3][i3]
        aux4 = matrix[i4][3]

        matrix[0][i1] = aux2
        matrix[i2][0] = aux3
        matrix[3][i3] = aux4
        matrix[i4][3] = aux1

        i1 += 1
        i2 -= 1
        i3 -= 1
        i4 += 1

    aux1 = matrix[1][1]
    aux2 = matrix[2][1]
    aux3 = matrix[2][2]
    aux4 = matrix[1][2]

    matrix[1][1] = aux2
    matrix[2][1] = aux3
    matrix[2][2] = aux4
    matrix[1][2] = aux1

    return matrix


matrix = []
for i in range(0, 4):
    line = input()
    matrix.append(list(line))

password = []
for i in range(0, 4):
    line = input()
    password.append(list(line))

final = []
for i in range(0, 4):

    for j in range(0, 4):
        for k in range(0, 4):
            if(matrix[j][k] == 'X'):
                final.append(password[j][k])
                # print(password[j][k])

    matrix = rotaciona(matrix)

print(''.join(final))
