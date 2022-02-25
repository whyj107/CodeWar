# Weight for weight
# kata5
# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

# 나의 풀이
def order_weight0(strng):
    result = []
    for s in strng.split():
        result.append((s, sum(map(int, s))))
    result = sorted(result, key=lambda x: (x[1], x[0]))
    return ' '.join(i for i, j in result)

def order_weight1(strng):
    result = [(sum(map(int, s)), s) for s in strng.split()]
    return ' '.join(j for i, j in sorted(result))

# 최종☆
def order_weight(strng):
    return ' '.join(j for i, j in sorted([(sum(map(int, s)), s) for s in strng.split()]))

# 다른 사람의 풀이
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))

print(order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99")
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123") ==
                   "11 11 2000 10003 22 123 1234000 44444444 9999")
print(order_weight("") == "")




