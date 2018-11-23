n = int(input())
labirinto = []

def visible_places(j, k):

    if (labirinto[j][k] != '#') and labirinto[j][k] != '1':

        labirinto[j][k] = '1'

        if((j - 1) >= 0):
            visible_places(j - 1, k)
        if((k + 1) < n):
            visible_places(j, k + 1)
        if((j + 1) < n):
            visible_places(j + 1, k)
        if((k - 1) >= 0):
            visible_places(j, k - 1)

for i in range(0, n):
    labirinto.append(list(input()))

paredes = 0

visible_places(0, 0)
visible_places(n - 1, n - 1)

# Count the number of wallls
for j in range(0, n):
    for k in range(0, n):

        if(labirinto[j][k] != '#') and (labirinto[j][k] == '1'):

            # Verify the top of the square
            if((j - 1) < 0):
                paredes += 1
            elif(labirinto[j - 1][k] == '#'):
                paredes += 1

            # Verify the right of the square
            if((k + 1) == n):
                paredes += 1
            elif(labirinto[j][k + 1] == '#'):
                paredes += 1

            # Verify the bottom of the square
            if ((j + 1) == n):
                paredes += 1
            elif (labirinto[j + 1][k] == '#'):
                paredes += 1

            # Verify the left of the square
            if ((k - 1) < 0):
                paredes += 1
            elif (labirinto[j][k - 1] == '#'):
                paredes += 1

print((paredes - 4) * 9)