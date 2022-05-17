# Don't give me five!
# https://www.codewars.com/kata/5813d19765d81c592200001a/train/python

# 나의 풀이
def dont_give_me_five(start, end):
    return len([i for i in range(start, end+1) if '5' not in str(i)])

# 다른 사람의 풀이
def dont_give_me_five1(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))

print(dont_give_me_five(1, 9), 8)
print(dont_give_me_five(1, 90), 72)
print(dont_give_me_five(4, 17), 12)