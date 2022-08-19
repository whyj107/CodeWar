# How Many Numbers?
# https://www.codewars.com/kata/55d8aa568dec9fb9e200004a/train/python

# 풀이
def sel_number(n, d):
    if n // 10 < 0: return
    else:
        result = []
        for num in range(12, n + 1):
            lst = [int(i) for i in str(num)]
            if lst == sorted(lst) and sum(lst) == sum(set(lst)):
                cnt = 0
                for i in range(len(lst) - 1):
                    if lst[i + 1] - lst[i] <= d:
                        cnt += 1
                if cnt == len(lst) - 1:
                    result.append(num)
        return len(result)

print(sel_number(0, 1), 0 )
print(sel_number(3, 1), 0)
print(sel_number(13, 1), 1)
print(sel_number(15, 1), 1)
print(sel_number(20, 2), 2)
print(sel_number(47, 3), 12)