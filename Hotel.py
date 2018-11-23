def create_table(valor, linha, coluna, matrix):

    matrix[linha][coluna] = valor

    if(linha + 1 < n and coluna + 1 < n):
        return create_table(valor + 1, linha + 1, coluna + 1, matrix)
    else:
        return (matrix, valor + 1)


n = int(input())

matrix = [[0 for x in range(n)] for y in range(n)]
valor = 1

for j in range(0, n):
    for i in range(n - 1, -1, -1):

        if(matrix[j][i] == 0):
            matrix, valor = create_table(valor, j, i, matrix)

for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end='')
        print(' ', end='')
    print()