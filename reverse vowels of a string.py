s = list(s)
vowels = list("aeiouAEIOU")


def reverseVowels(s):

    def swap(s, i, j):
        s[i], s[j] = s[j], s[i]

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] not in vowels and s[right] not in vowels:
            left += 1
            right -= 1
        elif s[left] not in vowels and s[right] in vowels:
            left += 1
        elif s[left] in vowels and s[right] in vowels:
            swap(s, left, right)
            left += 1
            right -= 1
        elif s[left] in vowels and s[right] not in vowels:
            right -= 1

    return "".join(s)

print(reverseVowels("leetcode"))