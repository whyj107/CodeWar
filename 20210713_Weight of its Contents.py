# Weight of its Contents
# https://www.codewars.com/kata/53921994d8f00b93df000bea/train/python

# 나의 풀이 : 소수점 처리가 이상하다.
def content_weight0(bottle_weight, scale):
    scale = scale.split()
    return bottle_weight/(int(scale[0])+1)*(int(scale[0]) if scale[-1] == 'larger' else 1)

# 나누기를 뒤에 하면 됨
def content_weight(bottle_weight, scale):
    scale = scale.split()
    return bottle_weight*(int(scale[0]) if scale[-1] == 'larger' else 1)/(int(scale[0])+1)

# 다른 사람의 풀이
def content_weight1(bottle_weight, scale):
    a, _, c = scale.split(" ")
    return bottle_weight * int(a) / (int(a) + 1) if c == "larger" else bottle_weight / (int(a) + 1)

print(content_weight(120, "2 times larger"), 80)
print(content_weight(180, "2 times larger"), 120)
print(content_weight(500, "9 times larger"), 450)
print(content_weight(1000, "49 times larger"), 980)
print(content_weight(1000, "999 times larger"), 999)

print(content_weight(120, "2 times smaller"), 40)
print(content_weight(300, "2 times smaller"), 100)
print(content_weight(1000, "4 times smaller"), 200)
print(content_weight(1000, "49 times smaller"), 20)
print(content_weight(10000, "999 times smaller"), 10)