# Words to Hex
# https://www.codewars.com/kata/596e91b48c92ceff0c00001f/train/python

# 나의 풀이
def words_to_hex(words):
    result = []
    for word in words.split():
        tmp = ''.join([format(ord(w), 'x') for w in word[:3]])
        result.append('#'+ tmp + (6-len(tmp))*'0')
    return result

# 다른 사람의 풀이
def words_to_hex1(words):
    return [f"#{w[:3].hex():0<6}" for w in words.encode().split()]

print(words_to_hex("Hello, my name is Gary and I like cheese."),
                   ['#48656c', '#6d7900', '#6e616d', '#697300', '#476172', '#616e64', '#490000', '#6c696b', '#636865']);
print(words_to_hex("0123456789"), ['#303132']);
print(words_to_hex("ThisIsOneLongSentenceThatConsistsOfWords"), ['#546869']);
print(words_to_hex("Blah blah blah blaaaaaaaaaaaah"), ['#426c61', '#626c61', '#626c61', '#626c61']);
print(words_to_hex("&&&&& $$$$$ ^^^^^ @@@@@ ()()()()("),
                   ['#262626', '#242424', '#5e5e5e', '#404040', '#282928']);