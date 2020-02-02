


def repeatedStringMatch(A, B):
    divNum = (len(B) - 1) // len(A) + 1

    for i in range(2):
        if B in A * (divNum + i):
            return divNum + i

    return -1


if __name__ == "__main__":
    A = "abcd"
    B = "cdabcdab"
    print(repeatedStringMatch(A, B))

