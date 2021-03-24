# Count salutes
# https://www.codewars.com/kata/605ae9e1d2be8a0023b494ed/train/python

# 문제를 이해하는 것이 힘들다....
# 다른 사람의 풀이
def count_salutes(hallway):
    right = 0
    salutes = 0
    for p in hallway:
        if p == '>':
            right += 1
        if p == '<':
            salutes += 2*right
    return salutes

def count_salutes1(h):
    return sum(2*sum(k=='<'for k in h[i:])*(h[i]=='>')for i in range(len(h)))

print(count_salutes('>--->---<--<'), 8)
print(count_salutes('<----<---<-->'), 0)
print(count_salutes('>-<->-<'), 6)


