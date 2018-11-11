test_cases = int(input())

for j in range(0, test_cases):

    n = int(input())
    people = []

    # Pega todas as informações das pessoas e armazena em tuplas
    for k in range(0, n):

        string = input().split()
        name = string[0].split(sep=':')[0]
        class_person = string[1].split(sep='-')

        class_person.reverse()
        person = (class_person, name)
        people.append(person)

    people.sort()
    people.reverse()

    equals = []
    k = 0

    while(k < len(people)):

        if(k == len(people) - 1):
            print(people[k][1])
            k += 1
        elif((k < len(people) - 1) and (people[k][0] != people[k + 1][0]) and (equals == [])):
            print(people[k][1])
            k += 1
        elif((k < len(people) - 1) and (people[k][0] == people[k + 1][0])):

            equals.append(people[k])
            equals.append(people[k + 1])

            l = k + 2

            while(l < len(people)):

                if(people[k][0] == people[l][0]):
                    equals.append(people[l])
                    l += 1
                else:
                    break

            equals.sort()

            for p in equals:
                print(p[1])

            equals = []
            k = l


    print('==============================')
