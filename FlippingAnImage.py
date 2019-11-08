

def flipAndInvertImage(A):

    output = []

    for i in range(0,len(A)):
        ls = A[i][::-1]
        temp = []
        for j in ls:
            if j ==1 :
                j = 0
                temp.append(j)
            else:
                j = 1
                temp.append(j)
        output.append(temp)


    return output

A = [[1,1,0],[1,0,1],[0,0,0]]

print(flipAndInvertImage(A))



# Steps :
# 1.reverse the 2D list and store it in another list
# 2.convert 0 --> 1 and 1 --> 0 and store them in a temporary list ( temp )
# 3.append the temp list to the output list
