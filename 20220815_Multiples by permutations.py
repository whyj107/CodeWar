# Multiples by permutations
# https://www.codewars.com/kata/55f1a53d9c77b0ed4100004e/train/python

# 나의 풀이
def search_permMult(nMax, k):
    result = []
    for i in range(1, nMax//2):
        if not i in result:
            if sorted(str(i*k)) == sorted(str(i)) and i*k <= nMax:
                result.append(i)
                result.append(i*k)
    return len(result)//2

# 다른 사람의 풀이
def search_permMult1(nMax, k):
    return len([1 for x in range(k, nMax, k) if sorted(str(x)) == sorted(str(x/k))])

print(search_permMult(10000, 7), 1)
print(search_permMult(5000, 7), 0)
print(search_permMult(10000, 4), 2)
print(search_permMult(8000, 4), 1)
print(search_permMult(5000, 3), 1)
print(search_permMult(10000, 3), 2)