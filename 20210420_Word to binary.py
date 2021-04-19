# Word to binary
# https://www.codewars.com/kata/59859f435f5d18ede7000050/train/python

# 나의 풀이
def word_to_bin(word):
    return [format(b, '08b') for b in bytearray(word, "utf8")]

# 다른 사람의 풀이
def word_to_bin1(word):
    return [f"{ord(c):08b}" for c in word ]

for word,exp in [ ('man', ['01101101', '01100001', '01101110']), ('AB', ['01000001', '01000010']),
        ('wecking',[ '01110111', '01100101', '01100011', '01101011', '01101001', '01101110', '01100111' ] ),
        ('Ruby',[ '01010010', '01110101', '01100010', '01111001']), ('Yosemite',[ '01011001', '01101111', '01110011', '01100101', '01101101', '01101001', '01110100', '01100101' ] ) ]:
        print(word_to_bin(word) == exp)

