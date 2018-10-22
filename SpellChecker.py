from sys import stdin as st

text = st.readlines()

list_text = []

errors = 0

end_line = True

for i in text:
    for word in i.split():
        list_text.append(word)

        #Verifica se a primeira letra de uma sentenca eh minuscula
        if(end_line == True):
            if(word[0].isupper() == False):
                errors = errors + 1

            if(word[len(word) - 1] != '.' and word[len(word) - 1] != '?' and word[len(word) - 1] != '!'):
                end_line == False
            else:
                end_line = True

        #Verifica se existe alguma letra maiuscula no meio da palavra
        for k in range(1, len(word)):
            if(word[k].isupper() == True):
                errors = errors + 1

print(errors)
