n = int(input())

for i in range(0, n):

    string = list(input())

    for k in range(1, len(string)):

        sub_string = string[0:k]

        if(len(sub_string) == len(string)):

            print(len(sub_string))

        for j in range(k, len(string)):

            print(string[j:k+1])

