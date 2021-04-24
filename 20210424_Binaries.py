# Binaries
# https://www.codewars.com/kata/5d98b6b38b0f6c001a461198/train/python

# 나의 풀이
dic = {'0': '10', '1': '11', '2': '0110', '3': '0111', '4': '001100',
       '5': '001101', '6': '001110', '7': '001111', '8': '00011000', '9': '00011001'}
def code(strng):
    return ''.join(dic[s] for s in strng)

def decode(strng):
    dic1 = dict(map(reversed, dic.items()))
    tmp = ""
    result = ""
    for s in strng:
        tmp += s
        if tmp in dic1.keys():
            result += dic1[tmp]
            tmp = ""
    return result

# 다른 사람의 풀이
def code1(stg):
    result = ""
    for d in stg:
        b = f"{int(d):b}"
        result = f"{result}{'0' * (len(b) - 1)}1{b}"
    return result
def decode1(stg):
    result = ""
    while stg:
        l = stg.find("1") + 1
        result, stg = f"{result}{int(stg[l:l*2], 2)}", stg[l*2:]
    return result


def testing_code(s, expected):
    actual = code(s)
    print(actual, expected)

def testing_decode(s, expected):
    actual = decode(s)
    print(actual, expected)

testing_code("62", "0011100110")
testing_code("55337700", "001101001101011101110011110011111010")
testing_code("1119441933000055", "1111110001100100110000110011000110010111011110101010001101001101")
testing_code("69", "00111000011001")
testing_code("86", "00011000001110")

testing_decode("10001111", "07")
testing_decode(
    "001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100",
    "444666333666777444")
testing_decode("01110111110001100100011000000110000011110011110111011100110000110001100110", "33198877334422")
testing_decode(
    "0011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111",
    "55500011144466666699919777777")
testing_decode(
    "01110111011111000110010011110011110011110011110011110011110111011101110110011001100110011001101111111010101100011001000110000001100000011000",
    "3331977777733322222211100019888")

