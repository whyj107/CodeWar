# up AND down
# https://www.codewars.com/kata/56cac350145912e68b0006f0/train/python

# 나의 풀이
def arrange(strng):
    strng = strng.split()
    pre = strng[0]
    result = [pre]

    for i in range(1, len(strng)-1):
        if len(pre) <= len(strng[i]) and len(strng[i]) >= len(strng[i+1]):
            result.append(pre)
            pre = strng[i-1]
        else:
            result.append(strng[i+1])
            pre = strng[i+1]
    print(result)
    return '\n'

def testing(actual, expected):
    print(actual, expected)

testing(arrange("who hit retaining The That a we taken"),
        "who RETAINING hit THAT a THE we TAKEN")  # 3
testing(arrange("on I came up were so grandmothers"), "i CAME on WERE up GRANDMOTHERS so")  # 4
testing(arrange("way the my wall them him"), "way THE my WALL him THEM")  # 1
testing(arrange("turn know great-aunts aunt look A to back"), "turn GREAT-AUNTS know AUNT a LOOK to BACK")  # 2
