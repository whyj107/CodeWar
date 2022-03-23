# How many pages in a book?
# https://www.codewars.com/kata/622de76d28bf330057cd6af8/train/python

# 나의 풀이
# 1~9           : 9
# 10~99         : 180
# 100~999       : 2,700
# 1000~9999     : 36,000
# 10000~99999   : 450,000

def amount_of_pages_0(summary):
    if summary < (9+1):
        tmp = summary
        return tmp//1
    elif summary < (9+180+1):
        tmp = summary - (9 - 1)
        return tmp//2 + 9
    elif summary < (9+180+2700+1):
        tmp = summary - (9 + 180 - 1)
        return tmp//3 + 99
    elif summary < (9+180+2700+36000+1):
        tmp = summary - (9 + 180 + 2700 - 1)
        return tmp//4 + 999
    else:
        tmp = summary - (9 + 180 + 2700 + 36000 - 1)
        return tmp//5 + 9999


def amount_of_pages(summary):
    a, b = 0, 0
    for i in range(0, 5):
        tmp = a+9 * (i*pow(10, (i-1)))
        if summary < (tmp+1):
            break
        a += 9 * (i*pow(10, (i-1)))
        b += 1
    return (summary - (a - 1))//b + (pow(10, b-1) - 1) if not summary<10 else summary


# 다른 사람의 풀이
def amount_of_pages1(summary):
    res = 0
    for x in range(1, 6):
        y = 9 * x * 10**(x-1)
        if summary <= y:
            return res + summary//x
        res += y//x
        summary -= y

print(amount_of_pages(5), 5)
print('--------------------')
print(amount_of_pages(25), 17)
print('--------------------')
print(amount_of_pages(1095), 401)
print('--------------------')
print(amount_of_pages(185), 97)
print('--------------------')
print(amount_of_pages(660), 256)
print('--------------------')
print(amount_of_pages(1275), 461)
print('--------------------')
print(amount_of_pages(133954), 29012)
