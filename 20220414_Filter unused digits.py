# Filter unused digits
# https://www.codewars.com/kata/55de6173a8fbe814ee000061/train/python

# 나의 풀이
def unused_digits(*l):
    result = "0123456789"
    for i in l:
        for j in str(i):
            result = result.replace(j, "")
    return result

# 다른 사람의 풀이
def unused_digits1(*args):
    return "".join(number for number in "0123456789" if number not in str(args))

def unused_digits2(*args):
    s =  ''.join(map(str,args))
    return ''.join(str(i) for i in range(0,10) if str(i) not in s)

print(unused_digits(12, 34, 56, 78), "09")
print(unused_digits(2015, 8, 26), "3479")
print(unused_digits(276, 575), "013489")
print(unused_digits(643), "0125789")
print(unused_digits(864, 896, 744), "01235")