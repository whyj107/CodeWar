# Calculator
# https://www.codewars.com/kata/5235c913397cbf2508000048/train/python

# 나의 풀이 : 이렇게 풀면 안된다 ㅋㅋㅋ
class Calculator0(object):
    def evaluate(self, string):
        return eval(string)

# () * ()일경우 오류남
class Calculator00(object):
    def evaluate(self, string):
        str = string.split()
        if string.count('(') > 0:
            o = str.index('(')
            c = len(str) - str[::-1].index(')') - 1
            tmp = str[o+1:c]
            tmp2 = self.evaluate(' '.join(tmp))
            del str[o:c]
            str[o] = tmp2
        while len(str) != 1:
            if str.count('/') > 0 and str.count('*') > 0:
                oper_index = min(str.index('/'), str.index('*'))
            elif str.count('/') > 0:
                oper_index = str.index('/')
            elif str.count('*') > 0:
                oper_index = str.index('*')
            else:
                oper_index = 1
            num1 = float(str[oper_index-1])
            num2 = float(str[oper_index+1])
            oper = str[oper_index]
            if oper == '+': num1 += num2
            elif oper == '-': num1 -= num2
            elif oper == '*': num1 *= num2
            elif oper == '/': num1 /= num2
            del str[oper_index:oper_index+2]
            str[oper_index-1] = num1
        return float(str[0])
    
class Calculator(object):
    def evaluate(self, string):
        strr = string.split()
        if string.count('(') > 0:
            while strr.count('(') != 0:
                c = strr.index(')')
                o = c - strr[:c][::-1].index('(') - 1
                tmp = strr[o+1:c]
                tmp2 = self.evaluate(' '.join([str(i) for i in tmp]))
                del strr[o:c]
                strr[o] = tmp2
        while len(strr) != 1:
            if strr.count('/') > 0 and strr.count('*') > 0:
                oper_index = min(strr.index('/'), strr.index('*'))
            elif strr.count('/') > 0:
                oper_index = strr.index('/')
            elif strr.count('*') > 0:
                oper_index = strr.index('*')
            else:
                oper_index = 1
            num1 = float(strr[oper_index-1])
            num2 = float(strr[oper_index+1])
            oper = strr[oper_index]
            if oper == '+': num1 += num2
            elif oper == '-': num1 -= num2
            elif oper == '*': num1 *= num2
            elif oper == '/': num1 /= num2
            del strr[oper_index:oper_index+2]
            strr[oper_index-1] = num1
        return float(strr[0])

# 다른 사람의 풀이
from operator import add, sub, mul, div

FIRST = {'*' : mul, '/': div}
SECOND = {'+': add, '-': sub}

class Calculator1(object):
    def evaluate(self, string):
        tokens = [float(t) if t.isdigit() or '.' in t else t for t in string.split()]
        while True:
            for (i, token) in enumerate(tokens):
                op = FIRST.get(token)
                if op:
                    tokens[i - 1 : i + 2] = [op(tokens[i - 1], tokens[i + 1])]
                    break
            else:
                ret = tokens[0]
                for i in xrange(1, len(tokens), 2):
                    ret = SECOND[tokens[i]](ret, tokens[i + 1])
                return ret if ret != 7.986000000000001 else 7.986 # Bug in test

# print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
# print(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
# print(Calculator().evaluate('1 + 1'), 2)
# print(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
# print(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
# print(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
# print(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)
print(Calculator().evaluate("1.1 + 2.2 + 3.3"), 6.6)
