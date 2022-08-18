# Numbers with The Highest Amount of Divisors
# https://www.codewars.com/kata/55ef57064cb8418a3f000061/train/python

# 나의 풀이
def proc_arrInt(listNum):
    p_n = {2:[]}
    for i in listNum:
        f = factors(i)
        if f in p_n.keys():
            p_n[f].append(i)
        else:
            p_n[f] = [i]
    max_n = max(p_n.keys())
    return [len(listNum), len(p_n[2]), [max_n, sorted(p_n[max_n])]]

def factors(n):
    result = set()
    for i in range(1, n//2+1):
        if n%i == 0:
            result.add(i)
            result.add(n//i)
    return len(result)

# 다른 사람의 풀이
def proc_arrInt1(lst):
    div_lst = [calu_divisors(x) for x in lst]
    maxdiv = max(div_lst)
    return [len(lst), div_lst.count(2), [maxdiv, sorted([x for i, x in enumerate(lst) if div_lst[i]==maxdiv])]]

def calu_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5) + 1):
        if num%i==0:
            divisors.append(i)
            divisors.append(num//i)
    return len(set(divisors))

arr1 = [66, 36, 49, 40, 73, 12, 77, 78, 76, 8, 50, 20, 85, 22, 24, 68, 26, 59, 92, 93, 30]
print(proc_arrInt(arr1), [21, 2, [9, [36]]])
arr2 = [267, 273, 271, 145, 275, 150, 487, 169, 428, 50, 314, 444, 445, 67, 458, 211, 58, 95, 357, 486, 359, 491, 108, 493, 247, 379]
print(proc_arrInt(arr2), [26, 7, [12, [108, 150, 444, 486]]])