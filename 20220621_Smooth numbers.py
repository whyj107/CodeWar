# Smooth numbers
# https://www.codewars.com/kata/5b2f6ad842b27ea689000082/train/python

# 나의 풀이
def is_smooth(n):
    f = max(factorization(n))
    result = {2: "power of 2", 3: "3-smooth", 5: "Hamming number", 7: "humble number"}
    return result.get(f, "non-smooth")

def factorization(n):
    d = 2
    result = []
    while d <= n:
        if n%d ==0:
            n //= d
            result.append(d)
        else:
            d += 1
            if d > 7:
                return [8]
    return result

# 소인수 분해
def factorization(n):
    d = 2
    result = []
    while d <= n:
        if n%d ==0:
            n //= d
            result.append(d)
        else:
            d += 1
    return result


print(is_smooth(16), "power of 2")
print(is_smooth(36), "3-smooth")
print(is_smooth(60), "Hamming number")
print(is_smooth(98), "humble number")
print(is_smooth(111), "non-smooth")
print(is_smooth(4096), "power of 2")
print(is_smooth(729), "3-smooth")
print(is_smooth(3125), "Hamming number")
print(is_smooth(7), "humble number")
print(is_smooth(17), "non-smooth")