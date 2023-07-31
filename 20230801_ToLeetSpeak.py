# ToLeetSpeak
# https://www.codewars.com/kata/57c1ab3949324c321600013f/train/python

# 나의 풀이
def to_leet_speak(str):
    dic = { 'A' : '@', 'B' : '8', 'C' : '(',
            'D' : 'D', 'E' : '3', 'F' : 'F',
            'G' : '6', 'H' : '#', 'I' : '!',
            'J' : 'J', 'K' : 'K', 'L' : '1',
            'M' : 'M', 'N' : 'N', 'O' : '0',
            'P' : 'P', 'Q' : 'Q', 'R' : 'R',
            'S' : '$', 'T' : '7', 'U' : 'U',
            'V' : 'V', 'W' : 'W', 'X' : 'X',
            'Y' : 'Y', 'Z' : '2', ' ' : ' '}
    return ''.join([dic[s] for s in str])

# 다른 사람의 풀이
def to_leet_speak1(str):
    return str.translate(str.maketrans("ABCEGHILOSTZ", "@8(36#!10$72"))

print(to_leet_speak("LEET"), "1337")
