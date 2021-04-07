# The Office VI - Sabbatical
# https://www.codewars.com/kata/57fe50d000d05166720000b1/train/python

# 나의 풀이 : 문제가 이해가 어려움
# s 안에 sabbatical이 있으면 1점 추가한다는 것
def sabb(s, val, happiness):
    sabbatical = (val + happiness + sum(1 for c in s if c in "sabbatical")) > 22
    return "Sabbatical! Boom!" if sabbatical else "Back to your desk, boy."

# 다른 사람의 풀이
SABBATICAL = set('sabbatical')
def sabb1(s, value, happiness):
    if value + happiness + sum(c in SABBATICAL for c in s) > 22:
        return 'Sabbatical! Boom!'
    else:
        return 'Back to your desk, boy.'

print(sabb("Can I have a sabbatical?", 5, 5), "Sabbatical! Boom!")
print(sabb("Why are you shouting?", 7, 2), "Back to your desk, boy.")
print(sabb("What do you mean I cant learn to code??", 8, 9), "Sabbatical! Boom!")
print(sabb("Please calm down", 9, 1), "Back to your desk, boy.")