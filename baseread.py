line = input()
while True:

    print(line)

    try:
        line = input()
    except EOFError:
        break
