from sys import stdin

for line in stdin:
    values = line.split()
    values = list(map(int, values))
    if values[-1] == -999999:
        del values[-1]
        localMax = values[0]
        localMin = values[0]
        result = values[0]
        # print(values)
        # print("AFTER::: Local Max: ", localMax, "Local Min: ", localMin, "result: ", result)
        for i in values[1:]:
            # print("aehoo", i)
            prevMax = localMax
            prevMin = localMin
            if i>=0:
                if prevMax*i > i:
                    localMax *= i
                else:
                    localMax = i
                if prevMin*i < i:
                    localMin *= i
                else:
                    localMin = i
            else:
                if prevMax*i < i:
                    localMin = prevMax*i
                else:
                    localMin = i
                if prevMin*i > i:
                    localMax = prevMin*i
                else:
                    localMax = i
            if result < localMax:
                result = localMax
            
            # print("AFTER::: Local Max: ", localMax, "Local Min: ", localMin, "result: ", result)
        
        print(result)