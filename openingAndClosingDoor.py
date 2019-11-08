

#use of stacks
#find number of pairs of closing and opening brackets


def openingAndClosingDoor(string):

    count = 0
    openBrackets = ["("]

    stack = []

    for i in string:
        if i in openBrackets:
            stack.append("(")

        else:
            if stack:
                if stack[-1] == openBrackets[0]:
                    stack.pop()
                    count+=1
            else:
                return -1

    if stack:
        return "invalid"

    return count


print(openingAndClosingDoor("()((()))()()"))