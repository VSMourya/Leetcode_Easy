



str = input("Enter string = ")

vowelList = ["A","E","I","O","U"]

string = ''

for i in range(0,len(str)):
    if str[i] in vowelList:
        for i in range(i,len(str)):
            string = string + str[i]
        break

print(string + "AY")