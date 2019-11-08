



def reverseWords(word):
    wordList = word.split(" ")
    lim = "."
    return lim.join(wordList[::-1])




inp = input("enter a sentence = ")


print(reverseWords(inp))

