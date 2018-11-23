n = int(input())

activities = []
for i in range(0, n):

    # Read activities times
    activities.append(list(map(int, input().split())))


# Sort the activities by your finish time
activities.sort(key=lambda x: x[1])

a = []
a.append(activities[0])
i = 0

for j in range(1, len(activities)):
    if(activities[j][0] > activities[i][1]):
        a.append(activities[j])
        i = j

print(len(a))