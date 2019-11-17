#
# Given a string s and an int k, return an int representing the number of substrings (not unique) of s
# with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.

def answer(s,k):

    ls = []

    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if len(set(s[i:j+1])) == k:
                ls.append(s[i:j+1])

    print(ls)
    return len(ls)


s = "pqpqs"
k = 2

print(answer(s,k))



