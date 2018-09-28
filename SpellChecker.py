line = input()

while True:

    print(line)

    try:
        line = input()
    except Exception as e:
        break
