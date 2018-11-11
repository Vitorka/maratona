t = int(input())

for i in range(0, t):

    line = input().split()
    if((line != '\n') and (line != '')):
        tam = int(line[0])
        palavra = line[1]

        tam = int(tam)

        strings = []

        aux = palavra[1:] + palavra[0]
        for j in range(1, tam):
            strings.append((aux, j))
            aux = aux[1:] + aux[0]

        strings.sort()
        print(strings[0][1])
