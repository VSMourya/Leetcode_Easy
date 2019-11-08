

#
# Steps:
#
# 1. Create a dictionary for mapping count values
# 2. return to same position is possible when
#    a. U = D and L = R
# 3. check U = D and L = R
#


def judgeCircle(moves):

    hsh = {"U" : 0,"D" : 0,"L" : 0,"R" : 0}

    for i in range(0,len(moves)):
        if moves[i] not in hsh:
            hsh[moves[i]] = 1
        else:
            hsh[moves[i]] += 1

    if hsh["U"] == hsh["D"] and hsh["L"] == hsh["R"]:
        return True
    else:
        return False


inp = input("Enter = ")
print(judgeCircle(inp))





































