t = int(input())

for i in range(0, t):

    line = input().split()
    n = int(line[0])

    vel = []

    for j in range(1, n + 1):
        vel.append(int(line[j]))

    max_vel = max(vel)

    print('Case {}: {}'.format(i + 1, max_vel))
