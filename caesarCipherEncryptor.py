



def caesarCipherEncryptor(string, key):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    finalString = []


    for i in range(0, len(string)):
        idx = alphabets.index(string[i])
        finalString.append(alphabets[(idx + key) % 26])

    output = "".join(finalString)

    return output


print(caesarCipherEncryptor("wtf",27))



