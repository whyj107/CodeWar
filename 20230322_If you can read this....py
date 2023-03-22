# If you can read this...
# https://www.codewars.com/kata/586538146b56991861000293/train/python

# 나의 풀이
NATO = {}
def to_nato(words):
    words = words.replace(' ', '')
    result = [NATO[w.upper()] if w.isalpha() else w for w in words]
    return ' '.join(result)

# 다른 사람의 풀이
def to_nato1(words):
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')

print(to_nato('If you can read'),
      "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
print(to_nato('Did not see that coming'),
      "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")
print(to_nato('.d?d!'), '. Delta ? Delta !')