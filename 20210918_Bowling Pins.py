# Bowling Pins
# https://www.codewars.com/kata/585cf93f6ad5e0d9bf000010/train/python

# 나의 풀이
def bowling_pins(arr):
    result = "6 7 8 9\n 3 4 5 \n  1 2  \n   0   "
    for a in reversed(sorted(arr)):
        result = result.replace(str(a-1), ' ')
    for i in range(9, -1, -1):
        if str(i) in result:
            result = result.replace(str(i), 'I')
    return result

# 다른 사람의 풀이
pins = "{7} {8} {9} {10}\n" + \
        " {4} {5} {6} \n" + \
         "  {2} {3}  \n" + \
          "   {1}   "

def bowling_pins1(arr):
    return pins.format(*(" " if i in arr else "I" for i in range(11)))

# print(bowling_pins([1, 2, 10]), "I I I  \n I I I \n    I  \n       ")
# print(bowling_pins([2, 3]), "I I I I\n I I I \n       \n   I   ")
print(bowling_pins([1, 2, 3, 4, 5, 6]), "I I I I\n       \n       \n       ")
