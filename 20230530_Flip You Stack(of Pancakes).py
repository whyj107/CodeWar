# Flip Your Stack (of Pancakes)
# https://www.codewars.com/kata/6472390e0d0bb1001d963536/train/python

# 다른사람의 풀이
def flip_pancakes(stack):
    tp, st, res = len(stack) - 1, stack[:], []

    while tp > 0:
        if st[tp] != max(st[:tp + 1]):
            ind = max(range(tp + 1), key=lambda k: st[k])
            st = st[ind + 1:tp + 1][::-1] + st[:ind + 1] + st[tp + 1:]
            res.extend([ind] * (ind > 0) + [tp])
        tp -= 1

    return res

def flip_pancakes1(stack):
    res = []

    while len(stack) != 0:
        if max(stack) == stack[-1]:
            stack.pop()

        elif stack.index(max(stack)) == 0:
            res.append(len(stack)-1)
            stack.reverse()

        else:
            a = stack[0: stack.index(max(stack)) + 1]
            res.append(stack.index(max(stack)))
            b = stack[stack.index(max(stack)) + 1:]
            a.reverse()
            stack = a + b
    return res


case1 = [1, 5, 8, 3]  ## [2,3,1]
case2 = [5, 1, 2, 3, 4]  ## [4,3]
case3 = [1, 2, 3, 5, 4]  ## [3,4,3,2]
case4 = list(range(1000, 0, -1))
## List in reverse order; can Pat do it? Answer = [9999]
# Duplicates
case5 = [2, 3, 1, 2, 4, 2]  ## [4,5,2,4,3,2]
case6 = [4, 1, 3, 2, 4, 6, 3, 9, 1]  ## [7,8,6,7,2,6,5,1,4,1,3]

tests = [case1, case2, case3, case4, case5, case6]
# tests = [case5, case6]

for elem in tests:
    print(elem, flip_pancakes(elem))

case1 = [1, 3, 5, 8]  ## Already sorted; answer = []
case2 = [1, 1, 1, 2, 2, 2]  ## Already sorted; answer = []
case3 = []  ## No pancakes - hungry! answer = []
case4 = [6]  ## 1 pancake; answer = []

tests = [case1, case2, case3, case4]

for elem in tests:
    print(elem, flip_pancakes(elem))
