# up AND down
# https://www.codewars.com/kata/56cac350145912e68b0006f0/train/python

# 나의 풀이
def arrange(strng):
    if strng == '': return ''
    strng = strng.split()
    result = []
    pre = strng[0]
    for i in range(1, len(strng)):
        if (len(pre) > len(strng[i]) and i%2 != 0) or (len(pre) < len(strng[i]) and i%2 == 0):
            result.append(strng[i])
        else:
            result.append(pre)
            pre = strng[i]
    result.append(pre)

    return ' '.join([r.lower() if idx%2 == 0 else r.upper() for idx, r in enumerate(result)])

# 다른 사람의 풀이
def arrange1(strng):
    words = strng.split()
    for i in range(len(words)):
        words[i:i+2] = sorted(words[i:i+2], key=len, reverse=i%2)
        words[i] = words[i].upper() if i%2 else words[i].lower()
    return ' '.join(words)

def testing(actual, expected):
    print(actual, expected)

testing(arrange("after be arrived two my so"),
        "be arrived two after my so")

"""
testing(arrange("who hit retaining The That a we taken"),
        "who RETAINING hit THAT a THE we TAKEN")  # 3
testing(arrange("on I came up were so grandmothers"),
        "i CAME on WERE up GRANDMOTHERS so")  # 4
testing(arrange("way the my wall them him"),
        "way THE my WALL him THEM")  # 1
testing(arrange("turn know great-aunts aunt look A to back"),
        "turn GREAT-AUNTS know AUNT a LOOK to BACK")  # 2
"""