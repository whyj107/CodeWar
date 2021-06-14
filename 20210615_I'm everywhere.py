# I'm everywhere!
# https://www.codewars.com/kata/6097a9f20d32c2000d0bdb98/train/python

# 나의 풀이
def i(word):
    tmp = sum(1 for w in word if w.lower() in 'aeiou')
    return 'Invalid word' if word.startswith('I') or tmp >= len(word)-tmp or word[0].islower() else f'i{word}'

# 다른 사람의 풀이
vowel = set("aeiouAEIOU").__contains__

def i1(word):
    if not word or word[0].islower() or word[0] == 'I' or 2*sum(map(vowel, word)) >= len(word):
        return "Invalid word"
    return 'i' + word

i2=lambda w:'i'+w if w and w<'Z'and len(w)>2*sum(map(w.lower().count,'aeiou'))and'I'!=w[0]else'Invalid word'

print(i('Phone'), 'iPhone')
print(i('World'), 'iWorld')
print(i('Human'), 'iHuman')
print(i('Programmer'), 'iProgrammer')
print(i(''), 'Invalid word')
print(i('Inspire'), 'Invalid word')
print(i('East'), 'Invalid word')
print(i('Peace'), 'Invalid word')
print(i('road'), 'Invalid word')