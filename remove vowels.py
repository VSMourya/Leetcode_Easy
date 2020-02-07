def removeVowels(S):
    res = ""

    hsh = set(list("aeiou"))

    for i in S:
        if i not in hsh:
            res += i

    return res

if __name__ == '__main__':
    a = "leetcodeisacommunityforcoders"
    print(removeVowels(a))