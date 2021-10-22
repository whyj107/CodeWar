# Bits Battle
# https://www.codewars.com/kata/58856a06760b85c4e6000055/train/python

# 나의 풀이
# 홀수의 1의 수가 짝수의 0보다 크면 승
def bits_battle(numbers):
    dic = {"odd": 0, "even": 0}
    for n in numbers:
        if n%2 == 0:
            dic["even"] += format(n, 'b').count('0')
        else:
            dic["odd"] += format(n, 'b').count('1')
    return 'odds win' if dic["odd"] > dic["even"] else ('evens win' if dic["odd"] < dic["even"] else 'tie')

# 다른 사람의 풀이
def bits_battle1(nums):
    binary = '{:b}'.format
    evens = odds = 0
    for num in nums:
        if num % 2:
            odds += binary(num).count('1')
        else:
            evens += binary(num).count('0')
    if odds == evens:
        return 'tie'
    return '{} win'.format('odds' if odds > evens else 'evens')

print(bits_battle([5, 3, 14]), 'odds win')
print(bits_battle([3, 8, 22, 15, 78]), 'evens win')
print(bits_battle([]), 'tie')
print(bits_battle([1, 13, 16]), 'tie')