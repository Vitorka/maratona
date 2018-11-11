n_words = int(input())
words = []
for i in range(0, n_words):
    words.append(input())

n_lines = int(input())
lines = []
for i in range(0, n_lines):
    lines.append(input())

flag = 0

for i in words:
    for j in range(0, len(lines)):

        if(i in lines[j]):
            print(j + 1, lines[j].find(i) + 1)
            flag = 1
            break

if(flag == 0):
    print("Passed")
