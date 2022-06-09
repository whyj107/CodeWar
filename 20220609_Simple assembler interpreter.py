# Simple assembler interpreter
# https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python

# 풀이
def simple_assembler(program):
    d, i = {}, 0
    while i < len(program):
        cmd, r, v = (program[i] + ' 0').split()[:3]
        if cmd == 'inc': d[r] += 1
        if cmd == 'dec': d[r] -= 1
        if cmd == 'mov': d[r] = d[v] if v in d else int(v)
        if cmd == 'jnz' and (d[r] if r in d else int(r)): i += int(v) - 1
        i += 1
    return d

code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
print(simple_assembler(code.splitlines()), {'a': 1})

code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
print(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})