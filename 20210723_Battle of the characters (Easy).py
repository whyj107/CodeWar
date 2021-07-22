# Battle of the characters (Easy)
# https://www.codewars.com/kata/595519279be6c575b5000016/train/python

# 나의 풀이
def battle(x, y):
    x_ = sum([ord(i)-64 for i in x])
    y_ = sum([ord(i)-64 for i in y])
    return 'Tie!' if x_ == y_ else (x if x_>y_ else y)

# 다른 사람의 풀이
def battle1(x, y):
    d={chr(i):c+1 for c,i in enumerate(range(65,91))}
    a=sum(d[c] for c in x)
    b=sum(d[c] for c in y)
    return 'Tie!' if a==b else [y,x][a>b]

print(battle("AAA", "Z"), "Z")
print(battle("ONE", "TWO"), "TWO")
print(battle("ONE", "NEO"), "Tie!")
print(battle("FOUR", "FIVE"), "FOUR")
print(battle("FREDAS", "TSOBES"), "TSOBES")