

# time - O(n)
# space - O(1)


def getValue(s,i):
    if s[i] == "I":
        if s[i + 1] == "V":
            return 4
        elif s[i + 1] == "X":
            return 9
        else:
            return 0

    elif s[i] == "X":
        if s[i + 1] == "L":
            return 40
        elif s[i + 1] == "C":
            return 90
        else:
            return 0

    elif s[i] == "C":
        if s[i + 1] == "D":
            return 400
        elif s[i + 1] == "M":
            return 900
        else:
            return 0


def romanToInt(s):

    hsh = {"I" : 1 ,"V" : 5 ,"X" :10 ,"L" :50 ,"C" :100 ,"D" :500 ,"M" :1000}           #constant space
    ls = {"I" ,"X" ,"C"}                                                                #constant space

    sm = 0
    i=0

    while i < len(s):
        if s[i] not in ls:
            sm += hsh[s[i]]
            i+=1
        else:
            if i != len(s)-1:
                val = getValue(s,i)
                if val != 0:
                    sm += getValue(s,i)
                    i+=2
                else:
                    sm += hsh[s[i]]
                    i+=1
            else:
                sm += hsh[s[i]]
                i+=1

    return sm


if __name__ == '__main__':
    s = "MCMXCIV"
    print(romanToInt(s))














