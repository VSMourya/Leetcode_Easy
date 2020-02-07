def twoSumLessThanK(A,K):

    A = sorted(A)

    left = 0
    right = len(A) - 1
    mx = -1

    while left < right:
        if A[left] + A[right] < K:
            mx = max(mx, A[left] + A[right])
            left += 1
        else:
            right -= 1

    return mx


if __name__ == '__main__':
    A = [34, 23, 1, 24, 75, 33, 54, 8]
    K = 60
    print(twoSumLessThanK(A,K))