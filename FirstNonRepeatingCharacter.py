#time - O(n)
#space - O(n)


str = "GeeksforGeeks"

target = 1
count = 0
set1 = {}


for char in str:
    if char not in set1:
        set1[char] = 1
    else:
        set1[char] +=1

for key,value in set1.items():

    if value == 1:
        count +=1
        if count == target:
            print("First Non repeating character is " + key)
        continue
    else:
        continue


#
# str = "GeeksforGeeks"
# print(str)
#
# countList = []
#
# for i in range(0,len(str)):
#     a = str[i]
#     count = 0
#     for j in range(0,len(str)):
#         if str[j] == a:
#             count += 1
#     countList.append(count)
#
#
#
# for i in range(0,len(str)):
#     if countList[i] == 1 :
#         print("the first non repeating number = " + str[i])
#         break
#     else:
#         continue
