# Wealth equality, finally!
# https://www.codewars.com/kata/5815f7e789063238b30001aa/train/python

# 나의 풀이
def redistribute_wealth(wealth):
    l = len(wealth)
    s = sum(wealth)
    for i in range(l):
        wealth[i] = s/l

# 다른 사람의 풀이
def redistribute_wealth1(wealth):
    wealth[:] = [sum(wealth) / len(wealth)] * len(wealth)

wealth_equal = [5, 5, 5, 5, 5]
wealth_unequal = [0, 10]
wealth_single = [5]
wealth_float = [3, 2, 2]

print(redistribute_wealth(wealth_equal), [5, 5, 5, 5, 5])
print(redistribute_wealth(wealth_unequal), [5, 5])
print(redistribute_wealth(wealth_single), [5])
print(redistribute_wealth(wealth_float), [2.3333333333333335, 2.3333333333333335, 2.3333333333333335])
