# Opposites Attract
# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

# 나의 풀이
def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2

# 다른 사람의 풀이
def lovefunc1(flower1, flower2):
    return (flower1+flower2) % 2

print(lovefunc(1, 4), True)
print(lovefunc(2, 2), False)
print(lovefunc(0, 1), True)
print(lovefunc(0, 0), False)