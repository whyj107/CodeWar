# The Barksdale Code
# https://www.codewars.com/kata/573d498eb90ccf20a000002a/train/python

# 나의 풀이
def decode(string):
    dict = {"0": "5", "1": "9", "2": "8", "3": "7", "4": "6",
            "5": "0", "6": "4", "7": "3", "8": "2", "9": "1"}
    return ''.join([dict[s] for s in string])

# 다른 사람의 풀이
def decode1(s):
    return s.translate(str.maketrans("1234567890", "9876043215"))

def decode2(string):
    return "".join(["5987604321"[int(char)] for char in string])

print(decode("4103432323"), "6957678787")
print(decode("4103438970"), "6957672135")
print(decode("4104305768"), "6956750342")
print(decode("4102204351"), "6958856709")
print(decode("4107056043"), "6953504567")