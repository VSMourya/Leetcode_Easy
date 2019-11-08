



houses = [[3, 7], [1, 9], [2, 0], [5, 15], [4, 30]]

houses.sort(key=lambda x:x[1])

print(houses)

store = []

for i in range(1,len(houses)):
    store.append(abs(houses[i-1][1]-houses[i][1]))

idx = store.index(max(store))

result = [houses[idx][0],houses[idx+1][0]]
result.sort()
print(result)