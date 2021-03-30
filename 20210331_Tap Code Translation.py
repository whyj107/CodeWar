# Tap Code Translation
# https://www.codewars.com/kata/605f5d33f38ca800322cb18f/train/python

# 나의 풀이
def tap_code_translation(text):
    dict = {'a': '. .', 'b': '. ..', 'c': '. ...', 'k': '. ...', 'd': '. ....', 'e': '. .....',
            'f': '.. .', 'g': '.. ..', 'h': '.. ...', 'i': '.. ....', 'j': '.. .....',
            'l': '... .', 'm': '... ..', 'n': '... ...', 'o': '... ....', 'p': '... .....',
            'q': '.... .', 'r': '.... ..', 's': '.... ...', 't': '.... ....', 'u': '.... .....',
            'v': '..... .', 'w': '..... ..', 'x': '..... ...', 'y': '..... ....', 'z': '..... .....'}
    return ' '.join([dict[t] for t in text])

# 다른 사람의 풀이
from string import ascii_lowercase as low
memo = {c:f"{'.'*(i//5+1)} {'.'*(i%5+1)}" for i, c in enumerate(low[:10]+low[11:])}
memo['k'] = memo['c']
def tap_code_translation1(text):
    return ' '.join(map(memo.get, text))

print(tap_code_translation("breaks"), ". .. .... .. . ..... . . . ... .... ...")
print(tap_code_translation("taps"), ".... .... . . ... ..... .... ...")
print(tap_code_translation("knocks"), ". ... ... ... ... .... . ... . ... .... ...")