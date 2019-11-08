



def busStops(ls):


    startPoint = ls[0]
    newLs = [ls[0]]

    for i in range(1,len(ls)):
        newLs.append(ls[i]-startPoint)

    return newLs


ls = [1,2,3]
print(busStops(ls))
