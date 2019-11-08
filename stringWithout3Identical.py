from itertools import groupby


def stringWithout3Identical(S):
    result = ""

    for alphabet, repeatTimes in groupby(S):
        L = len(list(repeatTimes))
        result += alphabet*(min(L,2))
    return result



S = 'eedaaad'
print(stringWithout3Identical(S))

S = 'xxxtxxx'
print(stringWithout3Identical(S))

S = 'uuuuxaaaaxuuu'
print(stringWithout3Identical(S))




