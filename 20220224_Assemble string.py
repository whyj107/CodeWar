# Assemble string
# https://www.codewars.com/kata/6210fb7aabf047000f3a3ad6/train/python
# kata6

# 나의 풀이
def assemble(input):
    result = list(input[0]) if input != [] else []
    for i in range(1, len(input)):
        for idx, j in enumerate(input[i]):
            if j == '*': continue
            result[idx] = j
    return ''.join(result).replace('*', '#')

# 다른 사람의 풀이
def assemble1(input):
    return ''.join(next((y for y in x if y != '*'), '#') for x in zip(*input))

print(assemble(['H*llo, W*rld!',
                'Hel*o, *or*d!',
                '*ello* World*']), 'Hello, World!')
print(assemble(['.** . ." ."" ! ! .', '. . . ." **" ! * .', '* . .*.* ."" * ! .', '. . .*." .**** ! .', '**. * .* .*" ! ! .']), '. . . ." ."" ! ! .')
print(assemble(['. . . .', '. . . .', '. . . .', '. . . .', '. . . .']), '. . . .')
print(assemble(['12***6789', '**3456789', '12345**8*', '***456**9', '1*3*5*7*9', '*2*456789']), '123456789')
print(assemble(['******', '******', '******', '******']), '######')
print(assemble(['*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*']), '###############')
print(assemble([]), '')