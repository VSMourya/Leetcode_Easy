from collections import Counter

def countCharacters(words,chars):

    def check(hsh1, hsh2):
        for key, value in hsh2.items():
            if hsh2[key] > hsh1[key]:
                return False
        return True

    count = 0
    hsh1 = Counter(chars)
    for i in words:
        hsh2 = Counter(i)
        if check(hsh1, hsh2):
            count += len(i)

    return count

if __name__ == '__main__':
    words = ["hello","wooorld","leetcode"]
    chars = "welldonehoneyr"
    print(countCharacters(words,chars))