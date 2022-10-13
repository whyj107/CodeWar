# Representing Numbers on an Abacus
# https://www.codewars.com/kata/60d7a52b57c9d50055b1a1f7/train/python

# 풀이
translate = { '0': '* - ****', '1': '* -* ***', '2': '* -** **', '3': '* -*** *', '4': '* -**** ',
             '5': ' *- ****', '6': ' *-* ***', '7': ' *-** **', '8': ' *-*** *', '9': ' *-**** '}

translate_rev = { '* - ****': '0', '* -* ***': '1', '* -** **': '2', '* -*** *': '3', '* -**** ': '4',
                  ' *- ****': '5', ' *-* ***': '6', ' *-** **': '7', ' *-*** *': '8', ' *-**** ': '9'}

def create_abacus(n):
    lenght = 9
    height = 8
    ans = ''
    n = str(n).zfill(lenght)
    for i in range(height):
        for num in n:
            ans += translate[num][i]
        ans += '\n'
    return ans[:-1]


def read_abacus(abacus):
    lenght = 9
    height = 8
    abaco = [''.join([abacus[i + (lenght + 1) * j] for j in range(height)]) for i in range(lenght)]

    ans = ''
    for el in abaco:
        ans += translate_rev[el]
    return int(ans)

print(create_abacus(3),
      '*********\n         \n---------\n        *\n*********\n*********\n******** \n*********')
print(create_abacus(7),
      '******** \n        *\n---------\n        *\n*********\n******** \n*********\n*********')
print(create_abacus(11),
      '*********\n         \n---------\n       **\n*******  \n*********\n*********\n*********')
print(create_abacus(1703),
      '****** **\n      *  \n---------\n     ** *\n***** ***\n****** **\n******** \n*********')
print(read_abacus('*********\n         \n---------\n        *\n*********\n*********\n******** \n*********'), 3)
print(read_abacus('******** \n        *\n---------\n        *\n*********\n******** \n*********\n*********'), 7)
print(read_abacus('*********\n         \n---------\n       **\n*******  \n*********\n*********\n*********'), 11)
print(read_abacus('****** **\n      *  \n---------\n     ** *\n***** ***\n****** **\n******** \n*********'), 1703)
