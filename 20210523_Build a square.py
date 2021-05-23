# Build a square
# https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python

# 나의 풀이
def generate_shape(n):
    return '\n'.join(['+'*n for i in range(n)])

# 다른 사람의 풀이
def generateShape1(i):
    return (i-1)*(('+'*i)+'\n')+('+'*i)

print(generate_shape(3), '+++\n+++\n+++')
print(generate_shape(8), '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++')