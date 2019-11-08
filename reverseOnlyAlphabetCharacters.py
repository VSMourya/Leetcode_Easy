
def swap(string,leftIdx,rightIdx):
    string[leftIdx],string[rightIdx] = string[rightIdx],string[leftIdx]

def convert(string):

    string = list(string)

    left = 0
    right = len(string)-1

    while left < right:

        leftValue = string[left]
        rightValue = string[right]

        if leftValue.isalpha():
            if rightValue.isalpha():
                string[left],string[right] = string[right],string[left]
                left+=1
                right-=1
            else:
                right-=1
        elif rightValue.isalpha():
            left+=1
        else:
            left+=1
            right-=1

    return "".join(string)


string = "agFE-dc-ba"

print(convert(string))