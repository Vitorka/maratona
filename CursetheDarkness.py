number_tests = int(input())

for i in range(0, number_tests):

    #Gets books location
    book = input().split()
    x_book = float(book[0])
    y_book = float(book[1])

    number_candles = int(input())

    flag = 0
    for j in range(0, number_candles):

        # Gets candles location
        candle = input().split()
        x_candle = float(candle[0])
        y_candle = float(candle[1])

        # Calc distance
        dist = ((x_candle - x_book)**2  + (y_candle - y_book)**2)**(1/2)

        if(dist <= 8.0000000):
            flag = 1

    if(flag == 1):
        print('light a candle')
    else:
        print('curse the darkness')