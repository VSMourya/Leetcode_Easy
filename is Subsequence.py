

def isSubsequence(s,t):
    i = 0
    for j in range(len(t)):

        if i >= len(s):
            return True

        if t[j] == s[i]:
            i += 1

    return True if i == len(s) else False


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s,t))







































