# Brainfuck generator
# https://www.codewars.com/kata/579e646353ba33cce2000093/train/python

# 풀이
# https://ko.wikipedia.org/wiki/%EB%B8%8C%EB%A0%88%EC%9D%B8%ED%8D%BD
def to_brainfuck0(string):
    return "".join(f"{'+' * ord(c)}.>" for c in string)


# 이게 정식 설명 같기도...
def bf_coord_char(n):
    b = n - (a := int(n ** .5)) ** 2
    return a, b


def bf_print_char(a, b):
    return f"{'+' * a}[>{'+' * a}<-]>{'+' * b}."


def to_brainfuck1(s):
    return '>'.join(bf_print_char(*bf_coord_char(ord(c))) for c in s)

# 이해하기는 이게 제일 쉬움
def to_brainfuck(string):
    res = ''
    prev_code = 0
    for char in string:
        code = ord(char)
        dif = prev_code - code
        if  dif < 0:
            res += ('+' * abs(dif))
        else:
            res += ('-' * dif)
        res += '.'
        prev_code = code
    return res

print(to_brainfuck("Hello World!"), "Hello World!")
print(to_brainfuck("Bye bye birdy"), "Bye bye birdy")
