# Sum of integers in string
# https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/python

# 나의 풀이
def sum_of_integers_in_string(s):
    cnt = []
    tmp = ''
    for i in s:
        if i.isdigit():
            tmp += i
        else:
            if tmp != '':
                cnt.append(int(tmp))
                tmp = ''
    if tmp != '':
        cnt.append(int(tmp))
    return sum(cnt)

# 다른 사람의 풀이
import re

def sum_of_integers_in_string1(s):
    return sum(int(x) for x in re.findall(r"(\d+)", s))


exampleTests = (
("12.4", 16),
("h3ll0w0rld", 3),
("2 + 3 = ", 5),
("Our company made approximately 1 million in gross revenue last quarter.", 1),
("The Great Depression lasted from 1929 to 1939.", 3868),
("Dogs are our best friends.", 0),
("C4t5 are 4m4z1ng.", 18),
("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635)
)

for testString, correctAnswer in exampleTests:
    print(sum_of_integers_in_string(testString), correctAnswer)