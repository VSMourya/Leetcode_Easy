



def coinsNeeded(arr,target):

    right = len(arr)-1
    coinsUsed = []

    while right >= 0:
        if target >= arr[right]:
            target = target - arr[right]
            coinsUsed.append(arr[right])
        elif target < arr[right]:
            right-=1

    return coinsUsed


arr = [1,2,5,10,20,50,100,200,500,1000]
target = 1294
print(coinsNeeded(arr,target))








