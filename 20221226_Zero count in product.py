# Zero count in product
# https://www.codewars.com/kata/639dd2efd424cc0016e7a611/train/python

# 나의 풀이
def zero_count(s):
    result = {}
    max_key = 0
    for i in range(s//3+1):
        for j in range(i, s//2+1):
            k = s-i-j
            if k < j: continue
            prod = i * j * k
            cnt = 0
            for _ in str(prod)[::-1]:
                if _ == '0': cnt += 1
                else: break
            if (cnt >= max_key) and ((i+j+k) == s):
                max_key = max(cnt, max_key)
                result.setdefault(cnt, [])
                result[cnt].append([i, j, k])
    return result[max_key]

# 다른 사람의 풀이
def zero_count1(sum):
    res = []
    max_zeros = 1
    for a in range(0, sum//3+1):
        for b in range(a, (sum-a)//2+1):
            c = sum - a - b
            prod = a * b * c
            zeros = 0
            while prod % 10 == 0:
                zeros += 1
                prod //= 10
                if prod == 0:
                    break
            if zeros == max_zeros:
                res.append([a,b,c])
            elif zeros > max_zeros:
                res = [[a,b,c]]
                max_zeros = zeros
    return res

print(zero_count(407) == [[32, 125, 250]])
print(zero_count(199) == [[10, 64, 125], [24, 25, 150], [24, 50, 125], [24, 75, 100], [34, 40, 125]])
print(zero_count(1) == [[0, 0, 1]])
print(zero_count(3) == [[0, 0, 3], [0, 1, 2]])
print(zero_count(376))