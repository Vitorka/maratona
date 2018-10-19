def LCS(seq1, seq2):

    #Matriz de scores
    v = [[0 for i in range(len(seq2) + 1)] for j in range(len(seq1) + 1)]

    for i in range(1, len(v)):
        for j in range(1, len(v[i])):
            if(seq1[i - 1] == seq2[j - 1]):
                v[i][j] = v[i - 1][j - 1] + 1
            else:
                v[i][j] = max(v[i][j - 1], v[i - 1][j])

    return v[len(seq1)][len(seq2)]

seq1 = input()
seq2 = input()

while True:

    seq1 = list(seq1)
    seq2 = list(seq2)

    print(LCS(seq1, seq2))

    try:
        seq1 = input()
        seq2 = input()
    except Exception as e:
        break




