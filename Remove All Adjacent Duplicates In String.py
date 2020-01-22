


def removeDuplicates(S):
    stack = []

    for i in S:
        if stack:
            if stack[-1] == i:
                stack.pop()
                continue
            else:
                stack.append(i)
        else:
            stack.append(i)

    return "".join(stack)



S= "abbaca"
print(removeDuplicates(S))


