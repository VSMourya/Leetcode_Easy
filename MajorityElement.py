

def MajorityElement(ls):

    countList = []
    for i in range(0, len(ls)):
        a = ls[i]
        count = 0
        for j in range(0, len(ls)):
            if ls[j] == a:
                count += 1
        countList.append(count)

    for j in range(len(countList)):
        if countList[j] > len(ls)//2 :
            return ls[j]

ls = [6,1,2,2,2,2,3]
print(MajorityElement(ls))


# OR

#if the repeating number repeats more than half the length of the list

#
# def MajorityElement(ls):
#
#     ls.sort()
#     return ls[len(ls)//2]
#
#
# ls = [6,1,2,2,2,2,3]
# print(MajorityElement(ls))
