# Which triangle is that?
# https://www.codewars.com/kata/564d398e2ecf66cec00000a9/train/python

# 나의 풀이
def type_of_triangle(a, b, c):
    try:
        if 2 * max([a, b, c]) < sum([a, b, c]):
            if a == b == c:
                return 'Equilateral'
            elif len(set([a, b, c])) == 2:
                return 'Isosceles'
            else:
                return 'Scalene'
        else:
            raise
    except:
        return 'Not a valid triangle'

# 다른 사람의 풀이
def type_of_triangle1(a, b, c):
    if type(a)==type(b)==type(c)==int and c<(a+b) and b<(a+c) and a<(b+c):
        if a==b==c:return "Equilateral"
        elif a==b or b==c or a==c:return "Isosceles"
        elif a!=b!=c:return "Scalene"
        else:return "Not a valid triangle"
    return "Not a valid triangle"

print(type_of_triangle(1,1,1), "Equilateral")
print(type_of_triangle(3,2,4), "Scalene")
print(type_of_triangle(2,2,1), "Isosceles")
print(type_of_triangle('.',5,82), "Not a valid triangle")