# Operations on sequences
# https://www.codewars.com/kata/5e4bb05b698ef0001e3344bc/train/python

# 나의 풀이
# 시간 초과된다.
def solve0(arr):
    p = 1
    for i in range(0, len(arr), 2):
        p *= (arr[i]**2 + arr[i+1]**2)
    a = 0
    b = (p - a ** 2) ** 0.5
    while int(b) != b:
        a += 1
        b = (p - a**2)**0.5
    return [a, int(b)]

# 다른 사람의 풀이
def solve1(arr):
    a, b, c, d = arr[0:4]
    #print(a, b, c, d)
    #print(arr[4:])
    first4 = [abs(a*c - b*d), (a*d+b*c)]
    if len(arr) == 4:
        return first4
    return solve(first4 + arr[4:])

'''
Using the identity 
(x² + y²)(u² + v²) = (xu + yv)² + (xv - yu)²
'''
def solve(arr):
    # your code
    print(arr)
    A = arr[0]
    B = arr[1]
    for i in range(2,len(arr),2):
        A_temp = A*arr[i] + B*arr[i+1]
        B = abs(A*arr[i+1] - B*arr[i])
        A = A_temp
    return [A,B]

def check(res, exp):
    if len(res) != 2:
        return False
    if res[0] < 0 or res[1] < 0 or type(res[0]) != int or type(res[1]) != int:
        print("A and B should be nonnegative integers")
        return False
    p = exp[0] ** 2 + exp[1] ** 2
    pp = res[0] ** 2 + res[1] ** 2
    if p != pp:
        print("Incorrect sum of squares")
        return False
    return True

def testing(arr, exp):
    ans = solve(arr)
    bl = check(ans, exp)
    print(bl, True)

a1 = [1, 3, 1, 2, 1, 5, 1, 9]
testing(a1, [250, 210])
a2 = [2, 1, 3, 4]
testing(a2, [2, 11])
a3 = [3, 9, 8, 4, 6, 8, 7, 8, 4, 8, 5, 6, 6, 4, 4, 5]
testing(a3, [13243200, 25905600])
