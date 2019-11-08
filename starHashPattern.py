
#starhashpattern

num = int(input())
if num==1:
    print("*")

for i in range(1,num):
    if i%2 == 1:
        print("*"*(i),end="#")
        print("#"*(num-i-1))
        if i == (num-1):
            print("*"*(num))
    if i % 2 == 0:
        a = "*" * (i)
        b = "#" * (num - i - 1)
        c = a+b
        print(c[::-1])

        if i == (num - 1):
            print("*" * (num))

#
# num = int(input())
# if num==1:
#     print("*")
#
# for i in range(1,num):
#         print("*"*(i),end="#")
#         print("#"*(num-i-1))
#         if i == (num-1):
#             print("*"*(num))
#
#





