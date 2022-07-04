# Rectangle letter juggling
# https://www.codewars.com/kata/60d6f2653cbec40007c92755/train/python

# 다른 사람의 풀이
import math
def cipher_text1(plain_text):
    text = "".join(c.lower() for c in plain_text if c.isalpha())

    s = math.sqrt(len(text))
    a = math.floor(s)
    b = math.ceil(s)
    if a * b < len(text):
        a = b

    return " ".join(text[i::b].ljust(a, " ") for i in range(b))

print(cipher_text1('When nobody is around, the trees gossip about the people who have walked under them.'))
print('wytotear hihstwlt eseshhkh natieoee nrrpphdm ooeaeau  buebovn  onsoped  ddgulwe ')

"""
print(cipher_text('I want a giraffe, but I\'m a turtle eating waffles.'),
                  'iiuril wrttne aailgs nfmew  tfaea  aetaf  gbutf ' )
print(cipher_text('Dolores wouldn\'t have eaten the meal if she had known what it actually was.'),
                  'dovhsoty oueehwaw llemenca odaehwts rntaahu  eteldaa  shniktl  watfnil ')
print(cipher_text('She says she has the ability to hear the soundtrack of your life.'),
                  'shaoscl hebhoki ehieuof salanfe asirdy  ytttto  shyhru  setear ')
print(cipher_text('I\'ve always wanted to go to Tajikistan, but my cat would miss me.'),
                  'isoiuom vwgktue eaoiml  antsyd  ltotcm  wetaai  adants  ytjbws ')
"""