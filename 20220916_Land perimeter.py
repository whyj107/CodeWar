# Land perimeter
# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python

# 나의 풀이
def land_perimeter(arr):
    result = 0
    for ar in arr:
        pre = ''
        for a in ar:
            if a == 'X':
                result += 4
                if pre == 'X':
                    result -= 2
            pre = a
    for ar in zip(*arr):
        pre = ''
        for a in ar:
            if a == 'X' and pre == 'X':
                result -= 2
            pre = a
    return f'Total land perimeter: {result}'


# 다른 사람의 풀이
def land_perimeter1(a):
    return 'Total land perimeter: ' + str(''.join(a).count('X') * 4 - sum(t == ('X','X') for r in a + zip(*a) for t in zip(r, r[1:])) * 2)

print(land_perimeter( ["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]), "Total land perimeter: 60")
print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), "Total land perimeter: 52")
print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]), "Total land perimeter: 40")
print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]), "Total land perimeter: 54")
print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]), "Total land perimeter: 40")