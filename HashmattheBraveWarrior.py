line = input()
while True:

    soldiers = line.split()
    hashmat = int(soldiers[0])
    opponent = int(soldiers[1])

    sub = hashmat - opponent

    if(sub < 0):
        print(sub * -1)
    else:
        print(sub)

    try:
        line = input()
    except Exception as e:
        break
