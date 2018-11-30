line = input()
while True:

    line = line.split()

    n = int(line[0])
    number_tracks = int(line[1])
    tracks = list(map(int, line[2:]))

    tracks.sort()

    for i in tracks:

        if(sum_tracks <= n):
            print('sum: {}'.format(sum_tracks))
            break
        sum_tracks -= i


    try:
        line = input()
    except EOFError:
        break
