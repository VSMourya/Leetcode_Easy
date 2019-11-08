
def validParentheses(myStr):

    stack = []

    openBrackets = ["(","[","{"]
    closedBrackets = [")","]","}"]

    for char in myStr:
        if char in openBrackets:
            stack.append(char)
        elif char in closedBrackets:
            pos = closedBrackets.index(char)
            if len(stack) > 0 and stack[-1] == openBrackets[pos]:
                stack.pop()
            else:
                return "unbalanced"

    if len(stack) == 0:
        return "balanced"
    else:
        return "false"


myStr = "(()"

print(validParentheses(myStr))
