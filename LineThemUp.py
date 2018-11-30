n = int(input())
names = []

for i in range(0, n):
    names.append(input())

# dec = names.copy()
# inc = names.copy()
#
# dec.sort(reverse=True)
# inc.sort()
#
# print(dec)
# print(inc)
# print(names)
#
# if(names == dec):
#     print('DECREASING')
# elif(names == inc):
#     print('INCREASING')
# else:
#     print('NEITHER')

if(names[0] > names[1]):
    antigo = 'DECREASING'
    novo = 'DECREASING'
else:
    antigo = 'INCREASING'
    novo = 'INCREASING'

if(n > 2):

    for i in range(2, n):

        if(names[i - 1] > names[i]):
            novo = 'DECREASING'
        else:
            novo = 'INCREASING'

        if(novo != antigo):
            novo = 'NEITHER'
            break

print(novo)