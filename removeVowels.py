

def removeVowels(string):
    ls = list("aeiou")

    final = ""

    for i in string:
        if i in ls:
            continue
        final += i

    return final


string = "faceprep"

print(removeVowels(string))
