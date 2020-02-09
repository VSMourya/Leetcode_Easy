def calculateTime(keyboard,word):
    hsh = {}
    keyboard = list(keyboard)

    for i in range(26):
        hsh[keyboard[i]] = i

    sm = 0
    start = 0
    for i in word:
        sm += abs(start - hsh[i])
        start = hsh[i]

    return sm


if __name__ == '__main__':
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "mourya"
    print(calculateTime(keyboard,word))


