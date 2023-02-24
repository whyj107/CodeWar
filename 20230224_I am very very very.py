# I am very very very....
# https://www.codewars.com/kata/58402cdc5225619d0c0000cb/train/python

# 풀이 : 다른 사람의 풀이 보고 만든 것
# 결국은 lambda를 사용해야 한다.
def iam(input=None, cnt=0):
    if input:
        return "I am " + "very "*cnt + input
    else:
        return lambda x=None: iam(x, cnt+1)

# 다른 사람의 풀이
# iam = lambda input=None, cnt=0: "I am " + "very "*cnt + input if input else lambda x=None: iam(x, cnt+1)

print(iam("happy"), "I am happy")
print(iam()("sad"), "I am very sad")
print(iam()()("tall"), "I am very very tall")
print(iam()()("tall and ") + iam()("funny"), "I am very very tall and I am very funny")

first, second = iam, iam
first = first()()
second = second()
first = first()
print(first("wild and ") + second("free"),
      "I am very very very wild and I am very free")

a = iam()()()()
b = a()()()
c = a()
t = a("happy and ") + b("big and ") + c("tall")
print(t, "I am very very very very happy and I am very very very very very very very big and I am very very very very very tall")
