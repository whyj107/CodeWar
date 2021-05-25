# An English Twist on a Japanese Classic
# https://www.codewars.com/kata/5b04be641839f1a0ab000151/train/python

# 나의 풀이
def game(words):
    result = []
    try:
        pre = words[0][-1]
        result.append(words[0])
        for i in range(1, len(words)):
            if words[i].startswith(pre):
                result.append(words[i])
                pre = words[i][-1]
            else:
                break
    except:
        pass
    return result

# 다른 사람의 풀이
def game1(words):
    i, link = 0, (words[0][0] if words and words[0] else None)
    for word in words:
        if link != word[:1]:
            break
        i, link = i+1, word[-1]
    return words[:i]

def game2(words):
    if not words or not words[0]:
        return []
    return [words[0]] + (game(words[1:]) if len(words) > 1 and words[1] and words[0][-1] == words[1][0] else [])

words = ["dog", "goose", "elephant", "tiger", "rhino", "orc", "cat"]
expected = ["dog", "goose", "elephant", "tiger", "rhino", "orc", "cat"]
print(game(words) == expected)