
#
# def segregate(ls):
#
#     count0 = 0
#     count1 = 0
#     for i in range(0,len(ls)):
#         if ls[i] == 0:
#             count0 += 1
#         else:
#             count1 += 1
#
#     newLs = [0]*count0 + [1]*count1
#
#     return newLs
#
# ls = [0,1,0,0,1,1,1,0,1,0]
#
# print(segregate(ls))

#OR


ls = [0,1,0,0,1,1,1,0,1,0]
ls.sort()
print(ls)
