# PhoneWords
# https://www.codewars.com/kata/635b8fa500fba2bef9189473/train/python

# 나의 풀이
from itertools import groupby
def phone_words(string_of_nums):
    result = ""
    phoneString = {'0': [' '], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    for _, g in groupby(string_of_nums):
        if _ == '1': continue
        idx = len(list(g))
        dic_len = len(phoneString[_])
        while idx > dic_len:
            result += phoneString[_][-1]
            idx -= (dic_len)
        result += phoneString[_][idx-1]
    return result

# 다른 사람의 풀이
import re
def phone_words1(str):
    ansd = {'0':' ','2':'a','22':'b','222':'c','3':'d','33':'e','333':'f',\
           '4':'g','44':'h','444':'i','5':'j','55':'k','555':'l','6':'m',\
           '66':'n','666':'o','7':'p','77':'q','777':'r','7777':'s','8':'t','88':'u',\
           '888':'v','9':'w','99':'x','999':'y','9999':'z'}
    ans=''
    for i in re.findall('0|2{1,3}|3{1,3}|4{1,3}|5{1,3}|6{1,3}|7{1,4}|8{1,3}|9{1,4}',str):
        ans+=ansd[i]
    return ans

KEYBOARD = {
    "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "
}
def phone_words2(str):
    ans = []
    for digit, sequence in filter(lambda x: x[0] != "1", groupby(str)):
        q, r = divmod(len(list(sequence)), len(KEYBOARD[digit]))
        if q: ans.append(KEYBOARD[digit][-1] * q)
        if r: ans.append(KEYBOARD[digit][r - 1])
    return "".join(ans)

print(phone_words("443355555566604466690277733099966688"), "hello how are you")
print(phone_words("55282"), "kata")
print(phone_words("44460208337777833777"), "im a tester")
print(phone_words("22266631339277717777"), "codewars")
print(phone_words("66885551555"), "null")
print(phone_words("833998"), "text")
print(phone_words("000"), "   ")
print(phone_words("7999844666166"), "python")
print(phone_words("55886444833"), "kumite")
print(phone_words("271755533"), "apple")
print(phone_words(""), "")
print(phone_words("111"), "")