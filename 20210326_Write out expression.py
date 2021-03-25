# Write out expression!
# https://www.codewars.com/kata/57e2afb6e108c01da000026e/train/python

# 나의 풀이
# 문제 속에 OPERATORS라고 주어져있었다. 바보 같았네
def expression_out(exp):
    oper = {'+': "Plus", '-': "Minus", '*': "Times", '/': "Divided By",
            '**': "To The Power Of", '=': "Equals", '!=': "Does Not Equal",
            '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
            '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}
    try:
        if not exp.split(' ')[1] in ['+', '-', '*', '/', '**', '=', '!=']: raise
        answer = ' '.join(oper[i] for i in exp.split(' '))
    except:
        answer = "That's not an operator!"
    return answer

# 다른 사람의 풀이
l = ['0','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
def expression_out1(exp):
    try:
        return l[int(exp.split()[0])] +" "+ OPERATORS[exp.split()[1]] + l[int(exp.split()[2])]
    except KeyError:
        return "That's not an operator!"

print(expression_out('1 + 3'), 'One Plus Three')
print(expression_out('2 - 10'), 'Two Minus Ten')
print(expression_out('6 ** 9'), 'Six To The Power Of Nine')
print(expression_out('5 = 5'), 'Five Equals Five')
print(expression_out('7 * 4'), 'Seven Times Four')
print(expression_out('2 / 2'), 'Two Divided By Two')
print(expression_out('8 != 5'), 'Eight Does Not Equal Five')


